from metric import Metric
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from threading import Thread
import time

from nltk.translate.bleu_score import corpus_bleu

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

        print("BLEU: Starting reference tokenization")
        list_of_reference_rows = self.input_data.split("\n")
        list_of_references = [[word_tokenize(row)] for row in list_of_reference_rows]
        print("BLEU: Done.")

        print("BLEU: Starting hypotheses tokenization")
        list_of_hypotheses_rows = self.output_data.split("\n")
        list_of_hypotheses = [word_tokenize(row) for row in list_of_hypotheses_rows]
        print("BLEU: Done.")
        
        print("BLEU: Starting BLEU calculation")
        score = corpus_bleu(list_of_references, list_of_hypotheses)
        print("BLEU: Done.")

        return score