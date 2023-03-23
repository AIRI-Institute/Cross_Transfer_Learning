# Response to Review #1:
Thank you for your detailed comments.

__Does data quality matter ?__

Hopefully so! An argument that supports this idea is the success of XLM-R when compared to the multilingual BERT model. One of the key contributors to this performance boost was the cleaner data preprocessing. Following this concern, we excluded from our corpus all the sources where language identification was made automatically.
However, our research focuses on an "out-of-the-wild" setting where we use reliable data without any specific cleaning. To simulate this scenario, we rely solely on high-quality language-diverse data resources that are typically a prerequisite for any transfer-learning study.
Therefore, the quality of our data is essential, and we concentrate on using data that is of conventional quality.

__Linguistic commonalities between HR and LR languages__
<TO DO>
  
__Does the script used by the language matter?__

Based on the data collected in our study, it is noticeable that the majority of the low-resource languages use the Latin script.
In order to consider this question more formally, we will include statistical tests for language script in the revised version (e.g. test in Section 4.9.1 in [BLOOM](https://arxiv.org/abs/2211.05100).

__Is it due to the way these languages are tokenized by mT5 tokenzer?__
  
The weaknesses of current models and especially the fertility of tokenizers ([Ács 2019](http://juditacs.github.io/2019/02/19/bert-tokenization-stats.html)) can hinder their effectiveness in certain languages, particularly those with an original script and limited resources.





# Response to Review #2:
Thank you for recognizing the novelties and advantages of our work.

__Question A: Data sampling for fine-tuning__

We conducted the model's fine-tuning on randomized data from various corpora. The objective was to tailor the model to perform well in high-resource languages, and generalization across multiple data sources is not our primary goal. Regarding evaluation, we assess the model performance of low-resource languages parsed from multiple corpora, as we said in Section 4.2.

__Question B: Early stopping and data in validation step__

As mentioned in Section 4.2, we incorporated data from high-resource languages to compute the validation loss. 
Indeed, the number of training steps has a significant influence on the transferability of the model. Regarding the early stopping, we saved checkpoints every 5% of the epoch and selected the best checkpoint based on the validation performance. Furthermore, we observed that prolonged training of the model could potentially cause overfitting to high-resource language and should be closely monitored to prevent it. We would be happy to include these valuable findings in the revision.

# Response to Review #3:
Thank you for your comments and interesting questions.

__Perplexity metric and downstream evaluation__

We understand your concerns about the perplexity metric and agree with its limitations in accurately measuring the "understanding" of language. As we noted in the limitations section, the need for labelled data for low-resource languages poses a challenge in addressing their syntactic and semantic aspects, at least in the case of experiments with transfer learning. Unfortunately, there are no labelled data for all 46 low-resource languages that we considered. Therefore, we cannot address the qualitative analysis of our experiments now.
However, for 7 of the 46 low-resource languages, a few samples are available in Universal Dependencies. These samples can be used to conduct model probing experiments, which can improve the interpretation of the results for at least some of the low-resource languages. Prior research on model probing has shown that these experiments can detect changes related to syntactic and semantic aspects after transfer learning. In the revised version of our work, we will provide more information on this point and present probing results on the Universal Dependencies data.

__lack of statistical significance tests__

Given our paper's extensive number of experiments, we acknowledge that comprehending all the presented data may be challenging. Therefore, statistical significance tests can aid in formalizing and clarifying the results. Our ideas for tests involve examining the correlation between transfer learning performance across various languages and linguistic characteristics of low-resource languages, utilizing the WALS features as an example (e.g. tests in Section 4.9.1 in [BLOOM](https://arxiv.org/abs/2211.05100)). We'll add it in the revision.

__Question A: Dialects in the list of LR languages__

Our results are derived from the language classification provided by WALS, where these two languages are treated as distinct. There are no dialects of high-resource languages within the list of 46 low-resource languages. 
Nevertheless, the question of differences between languages and dialects is very theoretical, with varying opinions on the status of certain languages. In this context, we have taken a practical approach and categorized languages into two groups on the number of resources available and not on their sociolinguistic statuses, as there are high-resource dialects (e.g. English dialects).

__Question B: Transfer learning between Formal Italian language and "Turinese"__

Thank you for your question! We believe that transfer learning across different languages and their dialects is promising for gaining linguistic insights. As both Italian and Turinese are well-resourced, it is feasible to carry out experiments in this area.


# General Response to Reviewers:
