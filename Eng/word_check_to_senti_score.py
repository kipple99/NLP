##################################### NL_processing_2.ipynb ##############################

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

df = pd.read_csv('NLP\imbd.tsv', delimiter='\\t')

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

# 보통 정제 작업에서 제거되는 단어들은 감성 지수가 중립인 경우가 많기 때문에 전체 결과에 큰 영향을 주지 않는다.
# 품사 태깅까지만 된 데이터를 가지고 분석 진행
# 필요 모듈 import
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from processing import penn_to_wn
nltk.download('wordnet')
nltk.download('sentiwordnet')
nltk.download('omw-1.4')

# 첫번째 로우로 감성 분석을 진행하고 해당 코드를 함수로 만들어 전체 데이터프레임에 적용

pos_tagged_words = df['pos_tagged_tokens'][0]
senti_score = 0

for word, tag in pos_tagged_words:
    # PennTreeBank 기준 품사를 WorNet 기준 품사로 변경
    wn_tag = penn_to_wn(tag)
    if wn_tag not in (wn.NOUN, wn.ADJ, wn.ADV, wn.VERB):
        continue
    
    # Synset 확인, 어휘 사전에 없을 경우에는 스킵
    if not wn.synsets(word, wn_tag):
        continue
    else:
        synsets = wn.synsets(word, wn_tag)
    
    # SentiSynset 확인
    synset = synsets[0]
    swn_synset = swn.senti_synset(synset.name())
    
    # 감성 지수 계산
    word_senti_score = (swn_synset.pos_score() - swn_synset.neg_score())
    senti_score += word_senti_score
    
##############################################################################

# 데이터 프레임의 각 로우에 저장되어있는 코퍼스들의 감성지수 확인

from processing import swn_polarity

# dataframe에 swn_polarity() 함수 적용
df['swn_sentiment'] = df['pos_tagged_tokens'].apply(swn_polarity)

