# Response to Review #1:

# Response to Review #2:


# Response to Review #3:
Thank you for your comments and interesting questions.

__Perplexity metric and downstream evaluation__

We understand your concerns about the perplexity metric and agree with its limitations in accurately measuring the "understanding" of language. As we noted in the limitations section, the lack of labeled data for low-resource languages poses a challenge in addressing their syntactic and semantic aspects at least in case of experiments with transfer learning. Unfortunately, there are no labeled data for all 46 low-resource languages that we considered, therefore, we cannot address to the qualitative analysis all of our experiments at this time.
However, for 7 of the 46 low-resource languages, there are a few samples available in Universal Dependencies. These samples can be used to conduct model probing experiments, which can improve the interpretation of the results for at least some of the low-resource languages. Prior research on model probing has shown that these experiments can detect changes related to syntactic and semantic aspects after transfer learning. In the revised version of our work, we will provide more information on this point and present probing results on the Universal Dependencies data.

__Lack of statistical significance tests__

Given the extensive number of experiments conducted in our paper, we acknowledge that comprehending all the presented data may be challenging. Therefore, statistical significance tests can aid in formalizing and clarifying the results. Our ideas for tests involve examining the correlation between transfer learning performance across various languages and linguistic characteristics of low-resource languages, utilizing the WALS features as an example (e.g. Section 4.9.1 in [BLOOM](https://arxiv.org/abs/2211.05100)). We’ll add it in the revision.

__Question A: Dialects in list on LR languages__ //
Our results are derived from the language classification provided by WALS, where these two languages are treated as distinct. Within the list of 46 low-resource languages, there are no dialects of high-resource languages. 
Nevertheless, the question of differences between languages and dialects is very theoretical, with varying opinions on the status of certain languages. In this context, we have taken a practical approach and categorized languages into two groups on the amount of resources available, and not on their sociolinguistic statuses, as there are high-resource dialects (e.g. English dialects).






# General Response to Reviewers:
