import nltk
from nltk.corpus import stopwords as sw
from nltk.tokenize import RegexpTokenizer

def tokenize_words(input_word):
    # regex for alphabetic sequences, special characters, and any other non-whitespace sequences
    tokenizer = RegexpTokenizer('\w[-\w]+|[!@#$%^&*(),.?":{}|<>]+|\S+')
    return tokenizer.tokenize(input_word)