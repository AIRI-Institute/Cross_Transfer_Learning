# Response to Review #1:
Thank you for your detailed comments.

__Does data quality matter ?__

Hopefully so! An argument supporting this idea is the success of XLM-R compared to the mBERT, where thorough data preprocessing plays a crucial role in the performance boost. Following this concern, we excluded sources where language identification was made automatically.
However, our research focuses on an "out-of-the-wild" setting where we use reliable data without any specific cleaning. To simulate this scenario, we rely solely on high-quality language-diverse data resources that are typically a prerequisite for any transfer-learning study.

Therefore, the quality of our data is essential, and we concentrate on using conventional quality data.

__Perplexity metric and downstream evaluation__

We understand your concerns about the perplexity metric and agree with its limitations in accurately measuring the "understanding" of language, which can be revealed on downstream tasks.
Unfortunately, to draw any conclusions regarding downstream results for the 46 LR languages we have examined, there is a need for more data (for example, there are several thousands of labelled sentences in Universal Dependencies for 7 low-resource languages). Hence, currently, we cannot address the qualitative analysis of our experiments related to the downstream evaluation of low-resource languages.
We will provide more information on this point in the revised version.


__Linguistic commonalities, Script and tokenization questions__

Thanks for these important questions! Indeed, we have not closely explored the reasons for such improvements.

Given our paper's extensive number of experiments, we understand that comprehending all the presented data may be challenging and agree that more interpretation is needed.
While most transfer learning studies focus on languages within the top hundred most popular ([Deshpande et al. 2022](https://aclanthology.org/2022.naacl-main.264.pdf), [Dolicki et al. 2021](https://arxiv.org/pdf/2105.05975.pdf)) and rely on downstream evaluations to interpret their findings, we face limitations to conduct the same setup due to the scarcity of labelled data required.
Therefore, statistical significance tests can aid in formalizing and clarifying the results in the case of extremely low-resource languages, which we considered. 
We have several ideas for tests, including examining the correlation between transfer learning performance and linguistic characteristics of low-resource languages using WALS features. Section 4.9.1 in [BLOOM](https://arxiv.org/abs/2211.05100) contains relevant tests. We'll add it in the revision.


__Question A: Did you verify any tokenization-based metrics to compare how "fair" the tokenization is between languages__

Regarding the work you mentioned ([Deshpande et al. 2022](https://aclanthology.org/2022.naacl-main.264.pdf)), the sub-word overlap is not a requirement for strong zero-shot transfer learning. In addition, prior work ([Lin et al. 2019](https://aclanthology.org/P19-1301.pdf)) stated that usually, the sub-word is omitted in case of low-resource languages due to insufficient data for sub-word extraction.
That is why we consider the statistical tests as the only formal method for interpreting this tendency with extremely low-resource languages, particularly in cases where downstream evaluation is not feasible for extremely LR languages.
We see now that this discussion should be clarified, and we will do so in the revision of the paper.


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

We understand your concerns about the perplexity metric and agree with its limitations in accurately measuring the "understanding" of language. As noted in the limitations section, the need for labelled data for LR languages poses a challenge in addressing their syntactic and semantic aspects. 
Unfortunately, to draw any conclusions regarding downstream results for the 46 low-resource languages we have examined, there is a need for more data (for example, there are maximum several thousands of labelled sentences in Universal Dependencies for 7 LR languages). Hence, currently, we cannot address the qualitative analysis of our experiments related to the downstream evaluation of LR languages.
We will provide more information on this point in the revised version.


__lack of statistical significance tests__

Given our paper's extensive number of experiments, we acknowledge that comprehending all the presented data may be challenging. Therefore, statistical significance tests can aid in formalizing and clarifying the results. 
We have several ideas for tests, including examining the correlation between transfer learning performance and linguistic characteristics of low-resource languages using WALS features. Section 4.9.1 in [BLOOM](https://arxiv.org/abs/2211.05100) contains relevant tests. We'll add it in the revision.

__Question A: Dialects in the list of LR languages__

Our results are derived from the language classification provided by WALS, where these two languages are treated as distinct. There are no dialects of HR languages within the list of 46 LR languages. 
Nevertheless, the question of differences between languages and dialects is very theoretical, with varying opinions on the status of certain languages. In this context, we have taken a practical approach and categorized languages into two groups on the number of resources available and not on their sociolinguistic statuses, as there are HR dialects (e.g. English dialects).


__Question B: Transfer learning between Formal Italian language and "Turinese"__

This is an interesting direction, but we did not consider it in this work. We believe that transfer learning across different languages and their dialects is promising for gaining linguistic insights. As both Italian and Turinese are well-resourced, it is possible to carry out experiments in this area.
