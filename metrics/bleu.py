from .metric import Metric
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from threading import Thread
import time

from nltk.translate.bleu_score import corpus_bleu
from nltk.translate.bleu_score import sentence_bleu
class Bleu_Metric(Metric):
    def get_score(self):
        # BLEU requires a list of references (Our original corpus)
        # and a list of hypotheses (our predicted lines)
        #
        # The length of those lists must be the same, meaning that the corpus 
        # and our predictions need exactly the same amount of lines
        #
        # TODO: Add solution for unequal lengths. Padding seems easiest.
        # TODO: BLEU rates empty lines with 0 score, even if correctly identified as empty lines

        reference = word_tokenize(self.input_data)
        hypothesis = word_tokenize(self.output_data)
        
        scores = dict()
        scores['BLEU-1'] = sentence_bleu([reference], hypothesis, weights=(1, 0, 0, 0))
        scores['BLEU-2'] = sentence_bleu([reference], hypothesis, weights=(0.5, 0.5, 0, 0))
        scores['BLEU-3'] = sentence_bleu([reference], hypothesis, weights=(1/3, 1/3, 1/3, 0))
        scores['BLEU-4'] = sentence_bleu([reference], hypothesis)

        return scores