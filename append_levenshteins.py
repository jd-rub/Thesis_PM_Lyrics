import hunspell
from numpy.core.defchararray import split
import pandas as pd

PATH = "./runs/markov/"
FILE_NAME = "markov.csv"

df = pd.read_csv(PATH + FILE_NAME)

all_words = []

for index, row in df.iterrows():
    all_words.append(row['hunspell_errors'])

flat_list = "".join([item for sublist in all_words for item in sublist]).replace("][", ",").replace('''"''', '\'').replace("','", "', '")

print('"' in flat_list)

splitlist = flat_list[2:].split("\', \'")

hs = hunspell.Hunspell()

tuples = []

from tqdm import tqdm
for word in tqdm(splitlist, desc="Loading Suggestions"):
    suggestions = hs.suggest(word)
    if(len(suggestions) > 0 and word != "<END>"):
        tuples.append([word, suggestions[0]])

print(tuples)

from Levenshtein import _levenshtein
def calc_levenshtein(tup):
    return _levenshtein.distance(tup[0], tup[1])

distances = [calc_levenshtein(tup) for tup in tqdm(tuples, "Calculating Distances")]

import pickle
with open(PATH + FILE_NAME + "-distances", "wb") as fp:
    pickle.dump(distances, fp)