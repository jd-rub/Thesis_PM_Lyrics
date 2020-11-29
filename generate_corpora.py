AMOUNT_STRINGS = 1000
INPUT_LENGTH = 8
OUTPUT_LENGTH = 2000
OUTPUT_PATH = "./runs/lstm-2048/"

import tensorflow as tf
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

import json
import pickle
with open("methods/data/alphabet.json", "rb") as fp:
    alphabet = json.load(fp)
chars = alphabet['allowed_chars']

# Generate random input strings
import random
def generate_random_string(alphabet=chars, length=INPUT_LENGTH):
    output = random.choices(alphabet, k=length)
    return "".join(output)

with open("./methods/clean_songs", "rb") as fp:
    corpus = pickle.load(fp)[:10]

length_distribution = [len(x) for x in corpus]

# with open("./run1/" + "inputs", "wb") as fp:
#     pickle.dump(input_strings, fp)

input_strings = []
for _ in range(AMOUNT_STRINGS):
    input_strings.append(generate_random_string())

# # MARKOV
from tqdm import tqdm
# from methods.markov.markov_adaptive_length import Markov_Adaptive
# markov = Markov_Adaptive(max_length=8)
# markov.load_models()
# markov_outputs = []
# for input in tqdm(input_strings, desc="Generating Markov outputs"):
#     # Draw Output length
#     output_length = random.choice(length_distribution)

#     generated_text = markov.generate_text(input, num_generate=output_length)
#     markov_outputs.append(generated_text[len(input):])
# print(markov_outputs[0])

# # LSTM
from methods.lstm.lstm_model import LSTM_Model
from methods.lstm.rnn_model import RNN_Config
lstm = LSTM_Model(RNN_Config(embedding_dim=256, batch_size=48, buffer_size=10000, rnn_units=2048, end_token="<END>"))
lstm.build_model()
lstm.load_trained_model_for_inference(checkpoint_path="methods/lstm/config_tests/2048/ckpt_11")

lstm_outputs = []
for input in tqdm(input_strings, desc="Generating LSTM outputs"):
        # Draw Output length
    output_length = random.choice(length_distribution)
    generated_text = lstm.generate_text(input, temperature=0.5, num_generate=output_length)
    lstm_outputs.append(generated_text)

import os
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

with open(OUTPUT_PATH + "inputs", "wb") as fp:
    pickle.dump(input_strings, fp)

# with open(OUTPUT_PATH + "markov", "wb") as fp:
#     pickle.dump(markov_outputs, fp)

with open(OUTPUT_PATH + "lstm", "wb") as fp:
    pickle.dump(lstm_outputs, fp)
