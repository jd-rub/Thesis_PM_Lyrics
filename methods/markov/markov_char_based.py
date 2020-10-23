from .helpers import weighted_choice
from scipy.sparse import dok_matrix
import pickle
from tqdm import tqdm

DEFAULT_K = 2

class Markov_Char():
    def __init__(self, k=DEFAULT_K):
        self.k = k
        
    def learn_corpus(self, corpus):
        # Create list of distinct characters
        self.distinct_chars = list(set(corpus)) #
        num_distinct_chars = len(self.distinct_chars)

        # Create distinct char indices
        char_idx_dict = {char: i for i, char in enumerate(self.distinct_chars)}

        # Create markov chains for every k
        sets_of_k_chars = [corpus[i:i+self.k] for i, _ in enumerate(corpus[:-self.k])]

        # Initialize next word matrix
        sets_count = len(list(set(sets_of_k_chars)))
        self.next_after_k_words_matrix = dok_matrix(
             (sets_count, num_distinct_chars)) #

         # Form unique_k_chars index dictionary
        distinct_set_of_k_chars = list(set(sets_of_k_chars))
        self.k_chars_idx_dict = {char: i for i, char in enumerate(distinct_set_of_k_chars)} #

        # Fill next char matrix
        for i, char in enumerate(tqdm(sets_of_k_chars[:-self.k], desc="Training Markov Model with k = " + str(self.k))):
            char_sequence_idx = self.k_chars_idx_dict[char]
            next_char_idx = char_idx_dict[corpus[i+self.k]]
            self.next_after_k_words_matrix[char_sequence_idx, next_char_idx] += 1

    def predict(self, seed):
        assert len(seed) == self.k, "Seed needs to be of length k = " + str(self.k)
        assert seed in self.k_chars_idx_dict.keys(), "Seed not found in corpus"

        next_char_vector = self.next_after_k_words_matrix[self.k_chars_idx_dict[seed]]
        likelihoods = next_char_vector/next_char_vector.sum()
        return weighted_choice(self.distinct_chars, likelihoods.toarray())

    def generate_text(self, start_string, num_generate=2):
        current_seed = start_string
        for _ in range(num_generate):
            start_string += self.predict(current_seed)
            current_seed = start_string[-self.k:]
        return start_string

    def save_to_disk(self, path = ""):
        if(path == ""):
            path = "./methods/markov/models/" + str(self.k)
        # Save generated matrix
        with open(path, "wb") as model_file:
            pickle.dump(self, model_file)
    
def load_from_file(path):
    with open(path, "rb") as model_file:
            return pickle.load(model_file)
