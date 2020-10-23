# Generate random input strings
AMOUNT_STRINGS = 10
INPUT_LENGTH = 8
OUTPUT_LENGTH = 1000

import json
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
"""
from methods.markov.markov_adaptive_length import Markov_Adaptive
markov = Markov_Adaptive(max_length=8)
markov.load_models()
markov_outputs = []
for input in input_strings:
    generated_text = markov.generate_text(input, num_generate=OUTPUT_LENGTH)
    markov_outputs.append(generated_text)
"""
# LSTM
from methods.lstm.lstm_model import LSTM_Model
lstm = LSTM_Model()
lstm.build_model()
lstm.load_trained_model_for_inference()

lstm_outputs = []
for input in input_strings:
    generated_text = lstm.generate_text(input, temperature=0.5)
    lstm_outputs.append(generated_text)

print(lstm_outputs)