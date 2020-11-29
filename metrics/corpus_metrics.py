from .smog import SMOG
from .flesch_kincaid import Flesch
from .hunspell_metric import Hunspell_Metric
from .grammar import Language_Tool_Metric

class Corpus_Metrics:
    def __init__(self, corpus):
        self.smog = SMOG(input_data=corpus)
        self.fleisch = Flesch(input_data=corpus)
        self.hunspell = Hunspell_Metric(input_data=corpus)
        self.grammar = Language_Tool_Metric(input_data=corpus)
        self.scores = dict()
        self.raw = dict()
        self.raw['text'] = corpus
    
    def calculate_metrics(self):
        self.scores['smog'] = self.smog.get_score()
        self.scores['flesch'] = self.fleisch.get_score()
        self.scores['hunspell'] = self.hunspell.get_score()
        self.scores['grammar'] = self.grammar.get_score()
        self.raw['smog'] = self.scores['smog']
        self.raw['flesch'] = self.scores['flesch']
        self.raw['hunspell'] = self.hunspell.incorrect_words
        self.raw['grammar'] = self.grammar.matches

# Testing corpus metrics
# import pickle
# with open("./run1/markov", "rb") as fp:
#     markov_corpus = pickle.load(fp)

# corpus = "".join(markov_corpus)
# metrics = Corpus_Metrics(corpus)
# metrics.calculate_metrics()
# print(str(metrics.scores))

# import pickle
# with open("./run1/lstm", "rb") as fp:
#     lstm_corpus = pickle.load(fp)

# corpus2 = "".join(lstm_corpus)
# metrics2 = Corpus_Metrics(corpus2)
# metrics2.calculate_metrics()
# print(str(metrics2.scores))