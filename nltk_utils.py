import nltk
from nltk.stem.porter import PorterStemmer

# nltk.download('punkt')
# nltk.download('punkt_tab')

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    pass

a = "¿Cuáles son mis derechos como estudiante?"
print(a)
a = tokenize(a)
print(a)