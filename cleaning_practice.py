import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from text import TEXT
nltk.download('punkt')

corpus = TEXT
tokenized_words = word_tokenize(corpus)

def clean_by_freq(tokenized_words, cut_off_count):
    vocab = Counter(tokenized_words)
    
    # 빈도수가 cut_off_count 이하인 단어를 제거하는 코드를 작성해 주세요
    uncommon_words = [key for key, value in vocab.items() if value <= cut_off_count]
    cleaned_words = [word for word in tokenized_words if word not in uncommon_words]
     
    return cleaned_words


def clean_by_len(tokenized_words, cut_off_length):
    cleaned_words = []
    
    for word in tokenized_words:
        # 길이가 cut_off_length 이하인 단어 제거하는 코드를 작성해주세요.
        if len(word) > cut_off_length:
            cleaned_words.append(word)
            
    return cleaned_words

    
# 조건에 맞게 함수 호출
clean_by_freq = clean_by_freq(tokenized_words, 2)
cleaned_words = clean_by_len(clean_by_freq, 2)

cleaned_words