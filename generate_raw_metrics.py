import pickle
CORPUS_PATH = "./runs/GPT-2-345M-50k/"
FILE_NAME = "short_songs"
with open(CORPUS_PATH + FILE_NAME, "rb") as fp:
    corpus = pickle.load(fp)

full_metrics = []

from metrics.corpus_metrics import Corpus_Metrics
from tqdm import tqdm
for i, text in tqdm(enumerate(corpus), desc="Calculating metrics"):
    try:
        text = text.replace("<END>", "\n")
        text = text.replace("<|endoftext|>", "\n")
        text = text.rsplit(" ", 1)[0]
        text = text[7:].split(" ", 1)[1]
        metrics = Corpus_Metrics(corpus=text)
        metrics.calculate_metrics()
        full_metrics.append(metrics.raw)
    except:
        print("Could not calculate metrics for text " + str(i))


import csv
try:
    with open(CORPUS_PATH + FILE_NAME + '.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['flesch', 'smog', 'hunspell', 'hunspell_errors', 'grammar', 'grammar_errors'])
        for row in full_metrics:
            writer.writerow([row['flesch'], row['smog'], len(row['hunspell']), row['hunspell'], len(row['grammar']), row['grammar']])
except:
    with open(CORPUS_PATH + FILE_NAME + '.pkl', 'wb') as fp:
        pickle.dump(full_metrics, fp)