from metric import Metric
from hunspell import Hunspell
from Levenshtein import _levenshtein
from nltk.tokenize import word_tokenize
import string
import time
h = Hunspell()
#h._system_encoding = 'UTF-8'

class Hunspell_Metric(Metric):
    correct_words = []
    incorrect_words = []
    full_data = [] # Tuples of [Original-Word, Hunspell-Suggestion, Levenshtein-Distance]
    has_done_work = False

    def do_work(self):
        starttime = time.time_ns() / 1000000000
        # Tokenize and find correct/incorrect words
        rows = self.output_data.split("\n")
        for row in rows:
            words = word_tokenize(row)
            tokens = list(filter(lambda token: token not in (string.punctuation + "“”…—``"), words))
            for token in tokens:
                if h.spell(token):
                    self.correct_words.append(token)
                else:
                    self.incorrect_words.append(token)
        time2 = time.time_ns() / 1000000000
        print("Done with tokens and spellcheck after", str(time2-starttime))
        # Sum Levenshtein distances of incorrect words
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
        time3 = time.time_ns() / 1000000000
        print("Done with Levenshtein after", str(time3-time2))
        self.has_done_work = True

    def get_score(self):
        if not self.has_done_work:
            self.do_work()
        return self.sum_distances


def calc_distance(w0, w1):
    return _levenshtein.distance(w0, w1)