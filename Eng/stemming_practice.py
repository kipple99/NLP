# 필요한 패키지와 함수 불러오기
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from text import TEXT
nltk.download('punkt')

corpus = TEXT
tokenized_words = word_tokenize(corpus)

# 포터 스테머의 어간 추출
def stemming_by_porter(tokenized_words):
    porter_stemmer = PorterStemmer()
    porter_stemmed_words = []

    for word in tokenized_words:
        # 여기에 코드를 작성하세요.
        stem = porter_stemmer.stem(word)
        porter_stemmed_words.append(stem)
            
    return porter_stemmed_words

stemming_by_porter(tokenized_words)
