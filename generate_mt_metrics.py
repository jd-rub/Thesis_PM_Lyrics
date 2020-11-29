import pickle
import pandas as pd
from tqdm import tqdm
from metrics.translation_metrics import Translation_Metrics

FOLDER_PATH = "runs/GPT-2-345M-50k/"

with open("runs/mt/tuples", "rb") as fp:
    tuples = pickle.load(fp)

def generate_GPT_metrics():
    with open(FOLDER_PATH + "mt_outputs", "rb") as fp:
        markov_tuples = pickle.load(fp)
    
    metrics = pd.DataFrame(columns=["BLEU-1", "BLEU-2", "BLEU-3", "BLEU-4", "ROUGE-1", "ROUGE-2", "ROUGE-L"])

    for i, tuple in tqdm(enumerate(markov_tuples)):
        reference = tuples[i][1]
        hypothesis = tuple.split("\n")[0]
        if len(hypothesis) < 3:
            hypothesis = tuple.split("\n")[1]
        trans_metrics = Translation_Metrics(hypothesis, reference)
        trans_metrics.calculate_metrics()

        row = {**trans_metrics.scores["bleu"], **trans_metrics.scores["rouge"]}

        metrics = metrics.append(row, ignore_index=True)
    
    metrics.to_csv(FOLDER_PATH + "mt_metrics.csv")



def generate_markov_metrics():
    with open("runs/GPT-2-117M-15k/mt_outputs", "rb") as fp:
        markov_tuples = pickle.load(fp)
    
    metrics = pd.DataFrame(columns=["BLEU-1", "BLEU-2", "BLEU-3", "BLEU-4", "ROUGE-1", "ROUGE-2", "ROUGE-L"])

    for i, tuple in tqdm(enumerate(markov_tuples)):
        reference = tuples[i][1]
        hypothesis = tuple[1]
        trans_metrics = Translation_Metrics(hypothesis, reference)
        trans_metrics.calculate_metrics()

        row = {**trans_metrics.scores["bleu"], **trans_metrics.scores["rouge"]}

        metrics = metrics.append(row, ignore_index=True)
    
    metrics.to_csv("runs/GPT-2-117M-15k/mt_metrics.csv")

def generate_lstm_1024_metrics():
    with open("runs/lstm/tupleslstm", "rb") as fp:
        lstm_tuples = pickle.load(fp)
    
    metrics = pd.DataFrame(columns=["BLEU-1", "BLEU-2", "BLEU-3", "BLEU-4", "ROUGE-1", "ROUGE-2", "ROUGE-L"])

    for i, tuple in tqdm(enumerate(lstm_tuples)):
        reference = tuples[i][1]
        hypothesis = tuple[1]
        trans_metrics = Translation_Metrics(hypothesis, reference)
        trans_metrics.calculate_metrics()

        row = {**trans_metrics.scores["bleu"], **trans_metrics.scores["rouge"]}

        metrics = metrics.append(row, ignore_index=True)
    
    metrics.to_csv("runs/lstm/mt_metrics.csv")

def generate_lstm_2048_metrics():
    with open("runs/lstm-2048/tupleslstm", "rb") as fp:
        lstm_tuples = pickle.load(fp)
    
    metrics = pd.DataFrame(columns=["BLEU-1", "BLEU-2", "BLEU-3", "BLEU-4", "ROUGE-1", "ROUGE-2", "ROUGE-L"])

    for i, tuple in tqdm(enumerate(lstm_tuples)):
        reference = tuples[i][1]
        hypothesis = tuple[1]
        trans_metrics = Translation_Metrics(hypothesis, reference)
        trans_metrics.calculate_metrics()

        row = {**trans_metrics.scores["bleu"], **trans_metrics.scores["rouge"]}

        metrics = metrics.append(row, ignore_index=True)
    
    metrics.to_csv("runs/lstm-2048/mt_metrics.csv")

generate_GPT_metrics()