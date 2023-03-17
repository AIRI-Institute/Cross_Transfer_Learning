import torch
from transformers import AutoConfig, AutoModel


class MLP(torch.nn.Module):
    def __init__(
        self, input_dim: int, num_classes: int, hidden_size: int, dropout_rate: float
    ):
        super(MLP, self).__init__()
        self.input_dim = input_dim
        self.hidden_size = hidden_size
        self.num_classes = num_classes
        self.dropout_rate = dropout_rate

        self.fc1 = torch.nn.Linear(self.input_dim, self.hidden_size)
        self.dropout = torch.nn.Dropout(self.dropout_rate)
        self.activation = torch.nn.Sigmoid()
        self.fc2 = torch.nn.Linear(self.hidden_size, self.num_classes)

    def forward(self, x: torch.Tensor):
        x = self.fc1(x)
        x = self.dropout(x)
        x = self.activation(x)
        x = self.fc2(x)
        return x


class ModelWithMLPClassifier(torch.nn.Module):
    def __init__(
        self,
        model_id: str,
        input_dim: int,
        num_classes: int,
        hidden_size: int,
        dropout_rate: float,
    ):
        super().__init__()
        config = AutoConfig.from_pretrained(
            model_id, output_attentions=True, output_hidden_states=True
        )
        self.model = AutoModel.from_pretrained(model_id, config=config)
        self.classifier = MLP(
            input_dim=input_dim,
            num_classes=num_classes,
            hidden_size=hidden_size,
            dropout_rate=dropout_rate,
        )

    def forward(self, **input):
        model_output = self.model(**input)
        cls_vector = model_output["hidden_states"][-1][:, 0, :]
        x = self.classifier(cls_vector)
        return x

    def freeze_model(self):
        for param in self.model.parameters():
            param.requires_grad = False

    def unfreeze_model(self):
        for param in self.model.parameters():
            param.requires_grad = True

    def freeze_classifier(self):
        for param in self.classifier.parameters():
            param.requires_grad = False

    def unfreeze_classifier(self):
        for param in self.classifier.parameters():
            param.requires_grad = True
