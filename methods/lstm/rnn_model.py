import tensorflow as tf

import numpy as np
import os
import time
import pickle

from .one_hot_encoding import Encoder

class RNN_Config():
    def __init__(self, embedding_dim, batch_size, buffer_size, rnn_units, end_token):
        self.embedding_dim = embedding_dim
        self.batch_size = batch_size
        self.buffer_size = buffer_size
        self.rnn_units = rnn_units
        self.end_token = end_token

DEFAULT_CONFIG = RNN_Config(embedding_dim=256, batch_size=64, buffer_size=10000, rnn_units=1024, end_token="<END>")
DEFAULT_ENCODER = Encoder()

class RNN_Model():
    def __init__(self, config=DEFAULT_CONFIG, encoder=DEFAULT_ENCODER):
        self.encoder = encoder
        self.model = tf.keras.Sequential()
        self.config = config
        self.vocab_size = len(self.encoder.encoding)

    def build_model(self):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Embedding(self.vocab_size, self.config.embedding_dim,
                                    batch_input_shape=[self.config.batch_size, None]),
            tf.keras.layers.GRU(self.config.rnn_units,
                                return_sequences=True,
                                stateful=True,
                                recurrent_initializer='glorot_uniform'),
            tf.keras.layers.Dense(self.vocab_size)
        ])

        self.model.compile(optimizer='adam', loss=self.loss)

    def train_model(self, text, epochs=10, seq_length=100, checkpoint_dir='methods/lstm/model_checkpoints'):
        text_as_int = self.encoder.encode_text(text)

        # Create training examples / targets
        char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

        # Convert slices into sequences of desired size
        sequences = char_dataset.batch(seq_length+1, drop_remainder=True)

        # Convert sequences into dataset with input and desired output
        dataset = sequences.map(split_input_target)

        # Convert dataset to trainable batches
        dataset = dataset.shuffle(self.config.buffer_size).batch(self.config.batch_size, drop_remainder=True)

        # Name of the checkpoint files
        checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

        checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
            filepath=checkpoint_prefix,
            save_weights_only=True)

        self.history = self.model.fit(dataset, epochs=epochs, callbacks=[checkpoint_callback])

    def loss(self, labels, logits):
        return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)

    # def load_weights_from_checkpoint(self, checkpoint_dir='methods/lstm/model_checkpoints'):
    #     self.build_model()

    def load_trained_model_for_inference(self, checkpoint_path=tf.train.latest_checkpoint('methods/lstm/lstm_checkpoints/')):
        self.config.batch_size = 1
        self.build_model()
        # self.model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))
        self.model.load_weights(checkpoint_path)
        self.model.build(tf.TensorShape([1, None]))

        print("Loaded trained model:")
        self.model.summary()

    def load_checkpoint(self, checkpoint_path):
        self.model.load_weights(checkpoint_path)

    def generate_text(self, start_string, num_generate=1000, temperature=1.0):
        # Evaluation step (generating text using the learned model)

        # num_generate: Number of characters to generate
        # temperature: Model temperature
        # Low temperature results in more predictable text.
        # Higher temperature results in more surprising text.
        # Experiment to find the best setting.

        # Converting our start string to numbers (vectorizing)
        input_eval = [self.encoder.encode(s) for s in start_string]
        input_eval = tf.expand_dims(input_eval, 0)

        # Empty string to store our results
        text_generated = []

        # Here batch size == 1
        self.model.reset_states()
        for _ in range(num_generate):
            predictions = self.model(input_eval)
            # remove the batch dimension
            predictions = tf.squeeze(predictions, 0)

            # using a categorical distribution to predict the character returned by the model
            predictions = predictions / temperature
            predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

            # Pass the predicted character as the next input to the model
            # along with the previous hidden state
            input_eval = tf.expand_dims([predicted_id], 0)

            text_generated.append(self.encoder.decode(predicted_id))

            if str(text_generated).endswith(self.config.end_token):
                break

        return (start_string + ''.join(text_generated))

    

def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text