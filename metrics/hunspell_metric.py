from .metric import Metric
from hunspell import Hunspell
from Levenshtein import _levenshtein
from nltk.tokenize import word_tokenize
import string
import time
from tqdm import tqdm
h = Hunspell()
#h._system_encoding = 'UTF-8'

class Hunspell_Metric(Metric):
    correct_words = []
    incorrect_words = []
    full_data = [] # Tuples of [Original-Word, Hunspell-Suggestion, Levenshtein-Distance]
    has_done_work = False

    def do_work(self):
        self.calculate_misspellings()
        self.calculate_distances()
        self.has_done_work = True

    def get_score(self):
        if not self.has_done_work:
            self.do_work()
        return self.sum_distances

    def calculate_misspellings(self):
        self.all_words = []
        # Tokenize and find correct/incorrect words
        rows = self.input_data.split("\n")
        for row in tqdm(rows, desc="Finding misspellings"):
            words = word_tokenize(row)
            self.all_words.append(words)
            tokens = list(filter(lambda token: token not in (string.punctuation + "“”…—``"), words))
            for token in tokens:
                if h.spell(token):
                    self.correct_words.append(token)
                else:
                    self.incorrect_words.append(token)

    def calculate_distances(self):
        self.sum_distances = 0
        for word in self.incorrect_words:
            suggestions = h.suggest(word)
            if len(suggestions) > 0:
                suggestion = suggestions[0]
                distance = calc_distance(word, suggestion)
                self.sum_distances += distance
                self.full_data.append([word, suggestion, distance])
            else:
                self.full_data.append([word, None, 0])


def calc_distance(w0, w1):
    return _levenshtein.distance(w0, w1)