# Generate random input strings
AMOUNT_STRINGS = 10
INPUT_LENGTH = 8
OUTPUT_LENGTH = 1000

import json
import pickle
with open("methods/data/alphabet.json", "rb") as fp:
    alphabet = json.load(fp)
chars = alphabet['allowed_chars']
print(chars)

import random
def generate_random_string(alphabet=chars, length=INPUT_LENGTH):
    output = random.choices(alphabet, k=length)
    return "".join(output)

input_strings = []
for _ in range(AMOUNT_STRINGS):
    input_strings.append(generate_random_string())

# MARKOV
from tqdm import tqdm
from methods.markov.markov_adaptive_length import Markov_Adaptive
markov = Markov_Adaptive(max_length=8)
markov.load_models()
markov_outputs = []
for input in tqdm(input_strings, desc="Generating Markov outputs"):
    generated_text = markov.generate_text(input, num_generate=OUTPUT_LENGTH)
    markov_outputs.append(generated_text)

# LSTM
from methods.lstm.lstm_model import LSTM_Model
lstm = LSTM_Model()
lstm.build_model()
lstm.load_trained_model_for_inference()

lstm_outputs = []
for input in tqdm(input_strings, desc="Generating LSTM outputs"):
    generated_text = lstm.generate_text(input, temperature=0.5)
    lstm_outputs.append(generated_text)

output_path = "/run1/"
import os

os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path + "inputs", "wb") as fp:
    pickle.dump(input_strings, fp)

with open(output_path + "markov", "wb") as fp:
    pickle.dump(markov_outputs, fp)

with open(output_path + "lstm", "wb") as fp:
    pickle.dump(lstm_outputs, fp)
