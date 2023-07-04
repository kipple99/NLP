from collections import Counter

# 등장 빈도 기준 정제 함수
def clean_by_freq(tokenized_words, cut_off_count):
    # 파이썬의 Counter 모듈을 통해 단어의 빈도수 카운트하여 단어 집합 생성
    vocab = Counter(tokenized_words)
    
    # 빈도수가 cut_off_count 이하인 단어 set 추출
    uncommon_words = {key for key, value in vocab.items() if value <= cut_off_count}
    
    # uncommon_words에 포함되지 않는 단어 리스트 생성
    cleaned_words = [word for word in tokenized_words if word not in uncommon_words]

    return cleaned_words

# 단어 길이 기준 정제 함수
def clean_by_len(tokenized_words, cut_off_length):
    # 길이가 cut_off_length 이하인 단어 제거
    cleaned_by_freq_len = []
    
    for word in tokenized_words:
        if len(word) > cut_off_length:
            cleaned_by_freq_len.append(word)

    return cleaned_by_freq_len

# 불용어 제거 함수
def clean_by_stopwords(tokenized_words, stop_words_set):
    cleaned_words = []
    
    for word in tokenized_words:
        if word not in stop_words_set:
            cleaned_words.append(word)
            
    return cleaned_words
