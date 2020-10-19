import pickle

class Encoder():
    def __init__(self):
        self.encoding = dict()
        self.decoding = dict()
        self.load_encoding()

    def load_encoding(self):
        if len(self.encoding) == 0:
            with open('methods/lstm/encoding', 'rb') as fp:
                self.encoding = pickle.load(fp)
                # self.decoding = {v: k for k, v in self.encoding.items()} # inverse dictionary of encoding
                self.decoding = [k for k, v in self.encoding.items()]

    def create_encoding(self):
        with open('methods/data/clean_songs', 'rb') as fp:
            songs = pickle.load(fp)

        encoding_ints = dict()

        for song in songs:
            for char in song:
                if char not in encoding_ints:
                    encoding_ints[char] = len(encoding_ints)

        with open('methods/lstm/encoding', 'wb') as fp:
            pickle.dump(encoding_ints, fp)

        self.encoding = encoding_ints

    def encode(self, character):
        if character in self.encoding:
            return self.encoding[character]
        else:
            raise KeyError(character)

    def decode(self, coded_char):
        if coded_char < len(self.encoding):
            return self.decoding[coded_char]
        else:
            raise KeyError(coded_char)

    def encode_text(self, text):
        encoded_text = []
        for c in text:
            encoded_text.append(self.encode(c))
        return encoded_text
    
    def decode_text(self, code):
        decoded_text = ""
        for n in code:
            decoded_text += self.decode(n)
        return decoded_text