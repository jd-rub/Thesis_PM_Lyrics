import pickle
import numpy as np

FILE_PATH = "./runs/markov/markov.csv-distances"
with open(FILE_PATH, "rb") as fp:
    distances = pickle.load(fp)

print(np.mean(distances))