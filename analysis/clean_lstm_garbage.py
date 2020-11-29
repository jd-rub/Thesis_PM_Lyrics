import pickle
PATH = "./runs/lstm-2048/"
FILE_NAME = "lstm"
with open(PATH + FILE_NAME, "rb") as fp:
    songs = pickle.load(fp)

from langdetect import detect
def get_lang(text):
    return detect(text)

good_songs = []
bad_songs = []
good_song_indices = []
for i, song in enumerate(songs):
    lang = get_lang(song)
    if lang == "en":
        good_songs.append(song)
        good_song_indices.append(i)
    else:
        bad_songs.append((lang, song))

# with open(PATH + "valid", "wb") as fp:
#     pickle.dump(good_songs, fp)

# with open(PATH + "invalid", "wb") as fp:
#     pickle.dump(bad_songs, fp)

import pandas as pd

metrics = pd.read_csv(PATH + FILE_NAME + ".csv")
good_metrics = metrics.iloc[good_song_indices]

good_metrics.to_csv(PATH + FILE_NAME + "-valid.csv")