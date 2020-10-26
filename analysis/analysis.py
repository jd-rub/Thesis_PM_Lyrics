CORPUS_PATH = "./run1/"
FILE_NAME = "markov.csv"

import pandas as pd

metrics = pd.read_csv(CORPUS_PATH + FILE_NAME)
averages = metrics.mean()
print(averages)