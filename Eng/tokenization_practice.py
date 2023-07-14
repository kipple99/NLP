import nltk
from text import TEXT
from nltk.tokenize import word_tokenize
nltk.download('punkt')

corpus = TEXT

tokenized_words = word_tokenize(corpus)

tokenized_words
