from methods.lstm.lstm_model import LSTM_Model
from methods.lstm.rnn_model import RNN_Config

with open("./corpus_clean.txt") as fp:
    text = fp.read()

model = LSTM_Model(RNN_Config(embedding_dim=256, batch_size=48, buffer_size=10000, rnn_units=2048, end_token="<END>"))

model.build_model()
model.model.summary()
model.train_model(text, epochs=20, checkpoint_dir="methods/lstm/config_tests/" + str(model.config.rnn_units) + "-2")