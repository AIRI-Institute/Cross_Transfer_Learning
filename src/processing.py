import json
import os
import pathlib
from typing import Dict, List, Tuple

import datasets
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from torch.utils.data import Dataset
from tqdm import tqdm


class DPTopicsDataset(Dataset):
    def __init__(
        self,
        data_path: pathlib.Path,
        sentence_column_name: str = "text",
        label_column_name: str = "topic",
        sep: str = ",",
    ) -> None:
        self.data_path = data_path
        self.data = pd.read_csv(data_path, sep=sep)

        self.sentence_list: List[str] = self.data[sentence_column_name].tolist()

        label_encoder = LabelEncoder()
        self.label_list: List[int] = label_encoder.fit_transform(
            self.data[label_column_name].tolist()
        )
        self._encoding = dict(
            zip(
                label_encoder.transform(label_encoder.classes_),
                label_encoder.classes_,
            )
        )

    def __len__(self):
        return self.data.shape[0]

    def __getitem__(self, idx: int) -> Tuple[str, int]:
        return self.sentence_list[idx], self.label_list[idx]


class MassiveDataset(Dataset):
    def __init__(
        self,
        data_path: pathlib.Path,
        sentence_column_name: str = "utt",
        label_column_name: str = "intent",
        partition_column_name: str = "partition",
    ) -> None:
        self.data_path = data_path
        self.sentence_column_name = sentence_column_name
        self.label_column_name = label_column_name
        self.partition_column_name = partition_column_name

        self.label_encoder = LabelEncoder()

        self.data = self.preprocess_massive()
        self._encoding = dict(
            zip(
                self.label_encoder.transform(self.label_encoder.classes_),
                self.label_encoder.classes_,
            )
        )

    def __len__(self):
        # Number of languages
        return len(self.data_path)

    def preprocess_massive(self) -> Dict[str, Dict[str, Dataset]]:
        datasets_dict = datasets.DatasetDict()
        for lang_file in tqdm(os.listdir(self.data_path)):
            lang_name = pathlib.Path(lang_file).stem
            lang_partition_dict: Dict[str, Dict[str, List[str]]] = {}
            with open(pathlib.Path(self.data_path, lang_file)) as f:
                for line in f:
                    data = json.loads(line)
                    partition = data[self.partition_column_name]

                    if partition not in lang_partition_dict:
                        lang_partition_dict[partition] = {
                            self.sentence_column_name: [],
                            self.label_column_name: [],
                        }

                    lang_partition_dict[partition][self.sentence_column_name].append(
                        data[self.sentence_column_name]
                    )

                    lang_partition_dict[partition][self.label_column_name].append(
                        data[self.label_column_name]
                    )

                if not hasattr(self.label_encoder, "classes_"):
                    encoded_labels = self.label_encoder.fit_transform(
                        lang_partition_dict[partition][self.label_column_name]
                    )
                else:
                    encoded_labels = self.label_encoder.transform(
                        lang_partition_dict[partition][self.label_column_name]
                    )
                lang_partition_dict[partition][self.label_column_name] = encoded_labels

            datasets_dict[lang_name] = {}
            for partition, lang_dict in lang_partition_dict.items():
                datasets_dict[lang_name][partition] = datasets.Dataset.from_dict(
                    lang_dict
                )
        return datasets_dict
