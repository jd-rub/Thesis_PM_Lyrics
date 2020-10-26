import pickle
CORPUS_PATH = "./run1/"
FILE_NAME = "lstm"
with open(CORPUS_PATH + FILE_NAME, "rb") as fp:
    corpus = pickle.load(fp)

# with open("./methods/clean_songs", "rb") as fp:
#     corpus = pickle.load(fp)

# corpus = corpus[:10]

full_metrics = []

from metrics.corpus_metrics import Corpus_Metrics
from tqdm import tqdm
for text in tqdm(corpus, desc="Calculating metrics"):
    metrics = Corpus_Metrics(corpus=text)
    metrics.calculate_metrics()
    full_metrics.append(metrics.scores)

import csv
with open(CORPUS_PATH + FILE_NAME + '.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['fleisch_kincaid', 'smog', 'hunspell', 'grammar'])
    for row in full_metrics:
        writer.writerow([row['fleisch_kincaid'], row['smog'], row['hunspell'], row['grammar']])
