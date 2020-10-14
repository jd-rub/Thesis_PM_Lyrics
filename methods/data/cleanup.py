import cleanup_helpers
import pickle
from tqdm import tqdm
from fix_corpus import fix_corpus

with open('methods/lstm/songs', 'rb') as fp:
    songs = pickle.load(fp)

clean_songs = []
bad_songs = []

for song in tqdm(songs):
    try:
        song = fix_corpus(song)
        cleanup_helpers.check(song)
        clean_songs.append(song)
    except Exception as ex:
        bad_songs.append([song, ex])

with open('methods/clean_songs', 'wb') as fp:
    pickle.dump(clean_songs, fp)

with open('methods/bad_songs', 'wb') as fp:
    pickle.dump(bad_songs, fp)