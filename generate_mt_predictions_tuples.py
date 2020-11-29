import pickle

with open("methods/data/clean_songs", "rb") as fp:
    songs = pickle.load(fp)

import random
def draw_random_row_tuple(songs, k):
    n_choices = random.choices(population=songs, k=k)
    
    tuples = []

    for song in n_choices:
        lines = song.split("\n")
        is_not_empty = False
        while not is_not_empty:
            if(len(lines) > 1):
                index = random.choice(range(len(lines[:-1])))
                if len(lines[index]) > 3 and len(lines[index+1]) > 3:
                    is_not_empty = True
                    tuples.append([lines[index], lines[index+1]])

    return tuples

tuples = draw_random_row_tuple(songs, 250)

with open("runs/mt/tuples", "wb") as fp:
    pickle.dump(tuples, fp)