import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np

# nltk.download('punkt')
# nltk.download('punkt_tab')

stemmer = PorterStemmer()


def tokenize(sentence):
    return nltk.word_tokenize(sentence.lower())


def stem(word):
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]

    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0

    return bag


# a = "¿Cuáles son mis derechos como estudiante?"
# print(a)
# a = tokenize(a)
# print(a)
