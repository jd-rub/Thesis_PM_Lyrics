# from rnn_model import RNN_Model
# from rnn_model import RNN_Config

# config = RNN_Config(embedding_dim=256, batch_size=64, buffer_size=10000, rnn_units=1024, end_token="<END>")

# rnn = RNN_Model()

text = ""
with open("corpus_clean.txt") as fp:
    text = fp.read()
# rnn.build_model()

# rnn.model.summary()

# rnn.train_model(text)
# rnn.load_trained_model('methods/lstm/model_checkpoints/ckpt_10')

# generated_text = rnn.generate_text(start_string="Fire in your heart", temperature=0.5)
# print(generated_text)

from lstm_model_testing import LSTM_Test
lstm = LSTM_Test()
lstm.build_model()

checkpoint_dir = 'methods/lstm/lstm2_checkpoints'

# lstm.model.summary()
# lstm.train_model(text, checkpoint_dir=checkpoint_dir, epochs=10)

lstm.load_trained_model_for_inference(checkpoint_dir+'/ckpt_10')
generated_text = lstm.generate_text(start_string="As ages pass", temperature=0.5)
print(generated_text)