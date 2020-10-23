from tensorflow.python.keras.layers.recurrent import LSTM
from .rnn_model import RNN_Model
import tensorflow as tf

class LSTM_Model(RNN_Model):
    def build_model(self):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Embedding(self.vocab_size, self.config.embedding_dim,
                                    batch_input_shape=[self.config.batch_size, None]),
            tf.keras.layers.LSTM(self.config.rnn_units,
                                return_sequences=True,
                                stateful=True,
                                recurrent_initializer='glorot_uniform'),
            tf.keras.layers.Dense(self.vocab_size)
        ])

        self.model.compile(optimizer='adam', loss=self.loss)