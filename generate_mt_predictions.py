import pickle
from tqdm import tqdm

MAX_LENGTH = 150

with open("runs/mt/tuples", "rb") as fp:
    tuples = pickle.load(fp)

def generate_markov():
    from methods.markov.markov_adaptive_length import Markov_Adaptive
    markov = Markov_Adaptive(max_length=8)
    markov.load_models()
    markov_outputs = []
    for input, reference in tqdm(tuples, desc="Generating Markov outputs"):
        output_length = MAX_LENGTH
        generated_text = markov.generate_text(input, num_generate=output_length)
        lines = generated_text.split("\n")
        markov_outputs.append(lines[:2])

    output_path = "runs/markov/tuples"

    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path + "markov", "wb") as fp:
        pickle.dump(markov_outputs, fp)

def generate_lstm_1024():
    from methods.lstm.lstm_model import LSTM_Model
    from methods.lstm.rnn_model import RNN_Config
    lstm = LSTM_Model(RNN_Config(embedding_dim=256, batch_size=48, buffer_size=10000, rnn_units=1024, end_token="<END>"))
    lstm.build_model()
    lstm.load_trained_model_for_inference(checkpoint_path="methods/lstm/config_tests/1024/ckpt_20")

    lstm_outputs = []
    for input, reference in tqdm(tuples, desc="Generating LSTM outputs"):
        output_length = MAX_LENGTH
        generated_text = lstm.generate_text(input, temperature=0.5, num_generate=output_length)
        lines = generated_text.split("\n")
        lstm_outputs.append(lines[:2])
    
    output_path = "runs/lstm/tuples"
    
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path + "lstm", "wb") as fp:
        pickle.dump(lstm_outputs, fp)

def generate_lstm_2048():
    from methods.lstm.lstm_model import LSTM_Model
    from methods.lstm.rnn_model import RNN_Config
    lstm = LSTM_Model(RNN_Config(embedding_dim=256, batch_size=48, buffer_size=10000, rnn_units=2048, end_token="<END>"))
    lstm.build_model()
    lstm.load_trained_model_for_inference(checkpoint_path="methods/lstm/config_tests/2048/ckpt_11")

    lstm_outputs = []
    for input, reference in tqdm(tuples, desc="Generating LSTM outputs"):
        output_length = MAX_LENGTH
        generated_text = lstm.generate_text(input, temperature=0.5, num_generate=output_length)
        lines = generated_text.split("\n")
        lstm_outputs.append(lines[:2])
    
    output_path = "runs/lstm-2048/tuples"
    
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path + "lstm", "wb") as fp:
        pickle.dump(lstm_outputs, fp)

generate_lstm_2048()