# Response to Review #1:

# Response to Review #2:


# Response to Review #3:
Thank you for your comments and interesting questions.

__Perplexity metric and downstream evaluation__

We understand your concerns about the perplexity metric and agree with its limitations in accurately measuring the "understanding" of language. As we noted in the limitations section, the lack of labeled data for low-resource languages poses a challenge in addressing their syntactic and semantic aspects at least in case of experiments with transfer learning. Unfortunately, there are no labeled data for all 46 low-resource languages that we considered, therefore, we cannot address to the qualitative analysis all of our experiments at this time.
However, for 7 of the 46 low-resource languages, there are a few samples available in Universal Dependencies. These samples can be used to conduct model probing experiments, which can improve the interpretation of the results for at least some of the low-resource languages. Prior research on model probing has shown that these experiments can detect changes related to syntactic and semantic aspects after transfer learning. In the revised version of our work, we will provide more information on this point and present probing results on the Universal Dependencies data.


# General Response to Reviewers:
