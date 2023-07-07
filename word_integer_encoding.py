# 정수 인코딩
# 전처리된 텍스트 데이터를 컴퓨터가 분석에 할용할 수 있게 하려면 숫자데이터로 변환
# 정수 인코딩 - 토큰화 된 각 단어에 특정 정수(코퍼스가 등장한 수)를 맵핑하여 고유 번호로 사용하는 방법

#############################################################################

# NL_processing_2.py
# 필요한 패키지와 함수 불러오기
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from collections import Counter
from text import TEXT
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
stopwords_set = set(stopwords.words('english'))

df = pd.read_csv('imbd.tsv', delimiter='\\t')

# 대소문자 통합
df['review'] = df['review'].str.lower() # 대소문자를 소문자로 바꾸는 과정

# 문장 토큰화
df['sent_tokens'] = df['review'].apply(sent_tokenize)
print(df['sent_tokens'][0])

# 품사 태깅
from processing import pos_tagger

df['pos_tagged_tokens'] = df['sent_tokens'].apply(pos_tagger)
print(df['pos_tagged_tokens'][0])
# 분석의 단위를 문장이 아니라 코퍼스로 하기 때문에 문장의 경계를 없앤 결과를 반환하도록 pos_tagger()를 만들었다.
# 만약 문장 간 구분을 한 상태에서 분석을 해야한다면 pos_tagger() 함수를 수정해서 필요한 상황에 맞게 사용하면 된다.

# 표제어 추출
# 품사가 태그된 단어 리스트를 활용하여 표제어 추출
from processing import words_lemmatizer

df['lemmatized_tokens'] = df['pos_tagged_tokens'].apply(words_lemmatizer)
print(df['lemmatized_tokens'][0])

from processing import clean_by_freq
from processing import clean_by_len
from processing import clean_by_stopwords
import processing # processing.py에서 stopwords 변수 불러오기

# 추가 전처리
# df['lemmatized_tokens']에서 빈도 1 이하, 단어 길이 2 이하인 단어 제거, 불용어 제거
df['cleaned_tokens'] = df['lemmatized_tokens'].apply(lambda x: clean_by_freq(x, 1)) # 빈도 1 이하 제거
df['cleaned_tokens'] = df['cleaned_tokens'].apply(lambda x: clean_by_len(x, 2)) #단어 길이 2 이하인 단어 제거
df['cleaned_tokens'] = df['cleaned_tokens'].apply(lambda x: clean_by_stopwords(x, stopwords_set)) # 불용어 제거

def combine(sentence):
    return ' '.join(sentence)
# 해당 리스트들을 토큰 구분이 없는 하나의 코퍼스로 통합

df['combined_corpus'] = df['cleaned_tokens'].apply(combine)

#############################################################################

# 하나의 로우 정수 인코딩
# 정수 인코딩을 하기 위해선 코퍼스에 포함된 단어 토큰들의 등장 빈도를 계산하여 빈도수가 높은 순서로 정렬해야함.
tokens = df['cleaned_tokens'][4]

vocab = Counter(tokens)
vocab = vocab.most_common()

print(vocab)

# 각 단어에 인덱스 부여
word_to_idx = {}
i = 0

for (word, frequency) in vocab:
    i = i + 1
    word_to_idx[word] = i

print(word_to_idx)

# 토큰 들을 부여된 인덱스로 바꾸기
encoded_idx = []

for token in tokens:
    idx = word_to_idx[token]
    encoded_idx.append(idx)
    
print(encoded_idx)

# 전체 데이터 프레임 정수 인코딩
tokens = sum(df['cleaned_tokens'], [])

print(tokens)

# 합쳐진 토큰리스트 빈도 계산, 많이 등장한 순으로 정렬 후 정수 인덱스 부여
word_to_idx = {}
i = 0
tokens = sum(df['cleaned_tokens'], [])

vocab = Counter(tokens)
vocab = vocab.most_common()

for (word, frequency) in vocab:
    i = i + 1
    word_to_idx[word] = i
    
print(word_to_idx)

# 데이터프레임의 토큰들을 정수 인코딩
def idx_encoder(tokens, word_to_idx):
    encoded_idx = []
    
    for token in tokens:
        idx = word_to_idx[token]
        encoded_idx.append(idx)
        
    return encoded_idx

df['integer_encoded'] = df['cleaned_tokens'].apply(lambda x: idx_encoder(x, word_to_idx))
df['integer_encoded']

# 모든 코퍼스의 토큰들에 정수 인덱스 부여 완료