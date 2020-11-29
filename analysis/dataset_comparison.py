import string
from tqdm import tqdm
import matplotlib.pyplot as plt

from nltk import download
from nltk.tokenize import TweetTokenizer, word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist

punctuation = []
punctuation += string.punctuation
punctuation.append('``')
punctuation.append("''")
punctuation.append('--')
punctuation.append('...')

# tokenizer = TweetTokenizer()
def remove_stopwords_and_punct(words):
    no_stop = [x.lower() for x in tqdm(words) if x.lower() not in set(stopwords.words('english'))]
    no_stop_no_punct = [x for x in tqdm(no_stop) if x not in punctuation]
    return no_stop_no_punct
def get_tokenized(words):
    words = words.lower()
    tokens = word_tokenize(words)
    contractions = {
        "'s": "is",
        "'re": "are",
        "n't": "not",
        "'m": "am",
        "'ll": "will",
        "ca": "can",
        "'ve": "have",
        "u": ""
    }
    long_forms = []
    for token in tokens:
        if token in contractions:
            long_forms.append(contractions[token])
        else:
            long_forms.append(token)
    
    return remove_stopwords_and_punct(long_forms)

def get_distribution(tokens):
    dist = FreqDist(tokens)
    return dist

from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

def get_lemmatized(words, pos="n"):
    lemmas = []
    for word in words:
        lemma = lem.lemmatize(word, pos)
        lemmas.append(lemma)
    return lemmas

# with open("./corpus_clean_no_tokens.txt") as fp:
#     songs = fp.read()
# tokenized_songs = get_tokenized(songs)

# lemmas = get_lemmatized(tokenized_songs)
# lemma_dist = get_distribution(lemmas)
# lemma_dist.plot(30, cumulative=False)


from nltk.corpus import brown
brown = brown.words()
brown_clean = remove_stopwords_and_punct(brown)
brown_lemma = get_lemmatized(brown_clean)
brown_dist = get_distribution(brown_lemma)
brown_dist.plot(30, cumulative=False)

plt.show()
# songs_dist = get_distribution(tokenized_songs)
# songs_dist.plot(30, cumulative=False)



# plt.show()



"""
def apply_softmax_to_tuples(tuples):
    words = np.array(tuples)[:, 0]
    dim = np.array(np.array(tuples)[:, 1], dtype=np.int)

    softmaxed_values = np.array([x / np.sum(dim) for x in dim])

    softmaxed_tuples = [(words[x], y) for x, y in enumerate(softmaxed_values)]

    return softmaxed_tuples

songs_most_common_words = np.array(songs_dist.most_common(100))[:, 0]

songs_softmaxed = apply_softmax_to_tuples(songs_dist.most_common(100))

songs_sum = np.sum(np.array(songs_dist.most_common(brown_dist.N()))[:, 1].astype(int))
brown_sum = np.sum(np.array(brown_dist.most_common(brown_dist.N()))[:, 1].astype(int))

x = np.array(songs_softmaxed)[:, 1]
y = np.array([brown_dist[word]/brown_sum for word in songs_most_common_words])

norm = plt.Normalize(1, 4)

fig, ax = plt.subplots()
sc = plt.scatter(np.flip(x), np.flip(y))

# annot = ax.annotate("", xy=(0,0), xytext=(20, 20), textcoords="offset points", bbox=dict(boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))
# annot.set_visible(False)

# def update_annot(ind):
#     pos = sc.get_offsets()[ind["ind"][0]]
#     annot.xy = pos
#     text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))), 
#                            " ".join([songs_most_common_words[n] for n in ind["ind"]]))
#     annot.set_text(text)
#     annot.get_bbox_patch().set_alpha(0.4)

# def hover(event):
#     vis = annot.get_visible()
#     if event.inaxes == ax:
#         cont, ind = sc.contains(event)
#         if cont:
#             update_annot(ind)
#             annot.set_visible(True)
#             fig.canvas.draw_idle()
#         else:
#             if vis:
#                 annot.set_visible(False)
#                 fig.canvas.draw_idle()

# fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()

print(songs_dist.most_common(100))
"""