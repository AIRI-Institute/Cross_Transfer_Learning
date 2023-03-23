# Response to Review #1:

# Response to Review #2:


# Response to Review #3:
Thank you for your comments and interesting questions.

__Perplexity metric and downstream evaluation__

We understand your concerns about the perplexity metric and agree with its limitations in accurately measuring the "understanding" of language. As we noted in the limitations section, the need for labelled data for low-resource languages poses a challenge in addressing their syntactic and semantic aspects, at least in the case of experiments with transfer learning. Unfortunately, there are no labelled data for all 46 low-resource languages that we considered. Therefore, we cannot address the qualitative analysis of our experiments now.
However, for 7 of the 46 low-resource languages, a few samples are available in Universal Dependencies. These samples can be used to conduct model probing experiments, which can improve the interpretation of the results for at least some of the low-resource languages. Prior research on model probing has shown that these experiments can detect changes related to syntactic and semantic aspects after transfer learning. In the revised version of our work, we will provide more information on this point and present probing results on the Universal Dependencies data.

__lack of statistical significance tests__

Given our paper's extensive number of experiments, we acknowledge that comprehending all the presented data may be challenging. Therefore, statistical significance tests can aid in formalizing and clarifying the results. Our ideas for tests involve examining the correlation between transfer learning performance across various languages and linguistic characteristics of low-resource languages, utilizing the WALS features as an example (e.g. Section 4.9.1 in [BLOOM](https://arxiv.org/abs/2211.05100)). We'll add it in the revision.

__Question A: Dialects in the list of LR languages__

Our results are derived from the language classification provided by WALS, where these two languages are treated as distinct. There are no dialects of high-resource languages within the list of 46 low-resource languages. 
Nevertheless, the question of differences between languages and dialects is very theoretical, with varying opinions on the status of certain languages. In this context, we have taken a practical approach and categorized languages into two groups on the number of resources available and not on their sociolinguistic statuses, as there are high-resource dialects (e.g. English dialects).

__Question B: Transfer learning between Formal Italian language and "Turinese"__

Thank you for your question! We believe that transfer learning across different languages and their dialects is promising for gaining linguistic insights. As both Italian and Turinese are well-resourced, it is feasible to carry out experiments in this area.


# General Response to Reviewers:
