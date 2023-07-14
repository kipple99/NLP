import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from text import TEXT
nltk.download('stopwords')
nltk.download('punkt')

corpus = TEXT
tokenized_words = word_tokenize(TEXT)

# NLTK에서 제공하는 불용어 목록을 세트 자료형으로 받아와 주세요
stopwords_set = set(stopwords.words('english'))

def clean_by_stopwords(tokenized_words, stopwords_set):
    cleaned_words = []

    for word in tokenized_words:
        # 여기에 코드를 작성하세요
        if word not in stopwords_set:
            cleaned_words.append(word)
    
    return cleaned_words

# 테스트 코드
clean_by_stopwords(tokenized_words, stopwords_set)
