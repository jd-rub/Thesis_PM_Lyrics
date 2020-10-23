import glob
import json

configraw = open("methods/lstm/config.json")
config = json.load(configraw)
end_of_song_token = config['endOfSongToken']

filenames = []
for file in glob.glob("genius/lyrics/*.json"):
    filenames.append(file)

jsonfiles = []
for file in filenames:
    jsonraw = open(file)
    jsonclean = json.load(jsonraw)
    jsonfiles.append(jsonclean)

songs = []

for artistjson in jsonfiles:
    for song in artistjson['songs']:
        if song['lyrics'] and len(song['lyrics']) > 20:
            songs.append(song['lyrics'])

import os
print(os.getcwd())

import sys
sys.path.insert(0, ".")
from methods.data.fix_corpus import fix_corpus

for i, song in enumerate(songs):
    song = fix_corpus(song)
    song += end_of_song_token
    songs[i] = song

import pickle
with open('methods/lstm/songs', 'wb') as fp:
    pickle.dump(songs, fp)
# f = open("methods/lstm/songs", "w", encoding='utf-8')
# f.write(str(songs))
# f.close()