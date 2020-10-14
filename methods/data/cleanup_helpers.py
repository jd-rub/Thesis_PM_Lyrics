import json
import string

def get_unknown_chars(text):
    fp = open("methods/data/alphabet.json")
    alphabet = "".join(json.load(fp)['allowed_chars'])
    alphabet += string.punctuation
    unknown_chars = [x for x in text if x not in alphabet]
    return unknown_chars

from langdetect import detect
def get_lang(text):
    return detect(text)

class UnknownCharException(Exception):
    def __init__(self, characters):
        self.characters = characters

class UnknownLanguageException(Exception):
    def __init__(self, language):
        self.language = language

class InvalidLengthException(Exception):
    def __init__(self, length):
        self.length = length

def check(text):
    # Check for length
    if len(text) < 50:
        raise InvalidLengthException(len(text))

    # Check for unknown characters
    unknown_chars = get_unknown_chars(text)
    if len(unknown_chars) != 0:
        raise UnknownCharException(unknown_chars)
    
    # Check for language
    language = get_lang(text)
    if language != "en":
        raise UnknownLanguageException(language)

    return True