from .metric import Metric
import hunspell
from Levenshtein import _levenshtein
from nltk.tokenize import word_tokenize
import string
import time
from tqdm import tqdm

class Hunspell_Metric(Metric):
    def __init__(self, input_data):
        super().__init__(input_data=input_data)
        self.hunspell = hunspell.Hunspell()

        self.correct_words = []
        self.incorrect_words = []
        self.full_data = [] # Tuples of [Original-Word, Hunspell-Suggestion, Levenshtein-Distance]
        self.has_done_work = False

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
        # for row in tqdm(rows, desc="Finding misspellings"):
        for row in rows:
            words = word_tokenize(row)
            self.all_words.append(words)
            tokens = list(filter(lambda token: token not in (string.punctuation + "“”…—``"), words))
            for token in tokens:
                if self.hunspell.spell(token):
                    self.correct_words.append(token)
                else:
                    self.incorrect_words.append(token)

    def calculate_distances(self):
        self.sum_distances = 0
        for word in self.incorrect_words:
            suggestions = self.hunspell.suggest(word)
            if len(suggestions) > 0:
                suggestion = suggestions[0]
                distance = calc_distance(word, suggestion)
                self.sum_distances += distance
                self.full_data.append([word, suggestion, distance])
            else:
                self.full_data.append([word, None, 0])


def calc_distance(w0, w1):
    return _levenshtein.distance(w0, w1)