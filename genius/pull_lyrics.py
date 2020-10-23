import lyricsgenius
import json
import threading

excluded_search_terms = ["(Live)", "(live)", "Acoustic", "acoustic", "remastered", "Remastered", "(demo)", "(Demo)", "(orchestral)", "(Orchestral)"]

def download_and_save_lyrics(artist_list, thread_num):
    genius = lyricsgenius.Genius("231Bx5as9znKdJrn6g3CHsg4T3Wdz4kABXr85cDGGNqOrg1xtm8kiyyLctH1Fs0m")
    genius.excluded_terms = excluded_search_terms
    genius.verbose = False
    genius.remove_section_headers = True
    genius.timeout = 50
    progress = 0
    for artist_name in artist_list:
        print("Thread" + str(thread_num) + ": Progress: " + str(progress))
        artist = genius.search_artist(artist_name)
        artist.save_lyrics()
        progress = progress + 10

artists_file = open('artists.json')
artists = json.load(artists_file)['artist_list']

thread_list = []

for n in range(0, 100, 10):
    t = threading.Thread(target=download_and_save_lyrics, args=(artists[n:(n+10)], int(n/10)))
    thread_list.append(t)
    t.start()

# download_and_save_lyrics(["TwilightForce"])