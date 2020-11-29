import pickle
PATH = "./runs/GPT-2-345M-50k/"
FILE_NAME = "texts"
MULT = 0.6 # 0.29 for all except 345-50k, there it is 0.6

with open(PATH + FILE_NAME, "rb") as fp:
    songs = pickle.load(fp)

import numpy as np
lengths = [len(x) for x in songs]
print(np.mean(lengths))

short_songs = [song[:int(len(song)*MULT)] for song in songs]


with open(PATH + "short_songs", "wb") as fp:
    pickle.dump(short_songs, fp)