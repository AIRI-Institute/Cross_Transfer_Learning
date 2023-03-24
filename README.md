# Response to Review #1:

Thank you for your detailed comments.

__Does data quality matter?__

Hopefully so! XLM-R's success supports this idea, as thorough data preprocessing plays a crucial role in a performance boost compared to mBERT.
Following this argument, we excluded sources with automatic language identification.
However, our research focuses on "out-of-the-wild" setting where we use reliable data without any specific cleaning. To simulate this scenario, we rely on high-quality language-diverse data resources that are typically a prerequisite for transfer learning study. Therefore, the quality of data is essential.

__Perplexity and downstream evaluation__

We agree that perplexity has limitations in measuring language "understanding", which, for example, can be revealed on downstream tasks.
Unfortunately, to draw any conclusions regarding downstream results for the 46 low-resource languages we have examined, there is a need for more data (for instance, there are only several thousands of labelled sentences in UD for 7 low-resource languages). Hence, currently, we cannot qualitatively analyze our experiments for downstream performance on extremely low-resource languages.
We'll provide more information on this point in the revised version.

__Linguistic commonalities, Script and tokenization questions__

Thanks for these important questions!
Given an extensive number of experiments, we agree that more interpretation is needed.
However, most transfer learning studies focus on languages within the top hundred most popular ([Deshpande et al. 2022](https://aclanthology.org/2022.naacl-main.264.pdf), [Dolicki et al. 2021](https://arxiv.org/pdf/2105.05975.pdf)) and rely on downstream evaluations to interpret their findings, we face limitations to conduct the same setup due to the scarcity of labelled data.
Therefore, statistical tests can aid in formalizing and clarifying the results in the case of extremely low-resource languages. 
We have several ideas for tests, including examining the correlation between transfer learning performance and linguistic characteristics of low-resource languages using WALS features (Section 4.9.1 in [BLOOM](https://arxiv.org/abs/2211.05100) contains relevant tests).
We'll add it in the revision.

__Question A: Did you verify any tokenization-based metrics to compare how "fair" the tokenization is between languages__

Regarding the work you mentioned ([Deshpande et al. 2022](https://aclanthology.org/2022.naacl-main.264.pdf)), considered sub-word overlap only in case of the downstream evaluations. In addition, prior work ([Lin et al. 2019](https://aclanthology.org/P19-1301.pdf)) stated that usually, the sub-word is omitted in case of low-resource languages due to insufficient data for sub-word extraction.
That is why we suggest statistical tests as the only formal method for interpreting this tendency with extremely low-resource languages, particularly in cases where downstream evaluation is not feasible.

We see now that this discussion should be clarified, and we'll do so in the revision of the paper.

# Response to Review #2:
Thank you for recognizing the novelties and advantages of our work.

__Question A: Data sampling for fine-tuning__

We conducted the model's fine-tuning to tailor it for high-resource language and used the randomized data from various corpora without aiming for generalization across multiple sources. Regarding evaluation, we assess the model performance of low-resource languages parsed from multiple corpora, as we said in Section 4.2.

__Question B: Early stopping and data in validation step__

As mentioned in Section 4.2, we incorporated data from high-resource languages to compute the validation loss. 
Indeed, the number of training steps significantly influences the model's transferability. Regarding the early stopping, we saved checkpoints every 5% of the epoch and selected the best checkpoint based on the validation performance. Furthermore, we observed that prolonged training could potentially cause overfitting to high-resource language and should be closely monitored to prevent it. We would be happy to include these findings in the revision.

# Response to Review #3:

Thank you for your comments and interesting questions.

__Perplexity and downstream evaluation__

We agree that perplexity has limitations in measuring language "understanding". As noted in Limitations, the need for labelled data for low-resource languages poses a challenge in addressing their syntactic and semantic aspects. 
Unfortunately, to draw any conclusions regarding downstream results for the 46 low-resource languages we have examined, there is a need for more data (for instance, there are only several thousands of labelled sentences in UD for 7 low-resource languages). Hence, currently, we cannot qualitatively analyze our experiments for downstream performance on extremely low-resource languages.
We'll provide more information on this point in the revised version.


__Lack of statistical tests__

Given an extensive number of experiments, we understand that comprehending all the presented results may be challenging and agree that more interpretation is needed. Therefore, statistical tests can aid in formalizing and clarifying the results. 
We have several ideas for tests, including examining the correlation between transfer learning performance and linguistic characteristics of low-resource languages using WALS features (Section 4.9.1 in [BLOOM](https://arxiv.org/abs/2211.05100) contains relevant tests). 
We'll add it in the revision.

__Question A: Dialects in the list of low-resource languages__

Our results are derived from language classification provided by WALS, where Italian and Turinese are treated as distinct. There are no dialects of high-resource languages within the list of 46 low-resource languages. 
Nevertheless, the question of differences between languages and dialects is very theoretical, with varying opinions on the status of certain languages. In this context, we have taken a practical approach and categorized languages into two groups on the number of resources available and not on their sociolinguistic statuses, as there are HR dialects (e.g. English dialects).


__Question B: Transfer learning between Italian and Turinese__

This is an interesting direction, but we didn't consider it in this work. We believe that transfer learning between languages and their dialects is promising for gaining linguistic insights. As both Italian and Turinese are well-resourced, it is possible to conduct experiments in this area.
