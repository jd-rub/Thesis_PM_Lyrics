CORPUS_PATH = "./runs/markov/"
FILE_NAME = "markov.csv"

import pandas as pd

metrics = pd.read_csv(CORPUS_PATH + FILE_NAME)
averages = metrics.mean()
print("AVERAGES:\n" + str(averages))