from .markov_char_based import Markov_Char

DEFAULT_KS = [1, 2, 4, 8, 16, 32, 64]
ks = [4, 8, 16]
file = open("corpus_clean.txt", encoding="utf-8")
corpus = file.read()

models = []
for k in ks:
    m = Markov_Char(k)
    m.learn_corpus(corpus)
    models.append(m)
    m.save_to_disk()
    print("Saved model with k = ", k)