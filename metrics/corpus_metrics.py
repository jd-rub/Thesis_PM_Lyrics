from .smog import SMOG
from .fleisch_kincaid import Fleisch_Kincaid
from .hunspell_metric import Hunspell_Metric
from .grammar import Language_Tool_Metric

class Corpus_Metrics:
    def __init__(self, corpus):
        self.smog = SMOG(input_data=corpus)
        self.fleisch_kincaid = Fleisch_Kincaid(input_data=corpus)
        self.hunspell = Hunspell_Metric(input_data=corpus)
        self.grammar = Language_Tool_Metric(input_data=corpus)
        self.scores = dict()
    
    def calculate_metrics(self):
        self.scores['smog'] = self.smog.get_score()
        self.scores['fleisch_kincaid'] = self.fleisch_kincaid.get_score()
        self.scores['hunspell'] = self.hunspell.get_score()
        self.scores['grammar'] = self.grammar.get_score()

# Testing corpus metrics
import pickle
with open("./run1/markov", "rb") as fp:
    markov_corpus = pickle.load(fp)

corpus = "".join(markov_corpus)
metrics = Corpus_Metrics(corpus)
metrics.calculate_metrics()
print(str(metrics.scores))

import pickle
with open("./run1/lstm", "rb") as fp:
    lstm_corpus = pickle.load(fp)

corpus2 = "".join(lstm_corpus)
metrics2 = Corpus_Metrics(corpus2)
metrics2.calculate_metrics()
print(str(metrics2.scores))