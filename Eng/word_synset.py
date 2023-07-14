# 필요한 패키지와 함수 불러오기
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from text import TEXT
from nltk.corpus import wordnet as wn
nltk.download('punkt')

synsets = wn.synsets('lead')
print(synsets)
# synset('단어, 품사, 순번')의 형태

# 각 순번에 해당하는 정확한 단어 의미 확인하기
print(wn.synset('lead.n.01').definition())
print(wn.synset('lead.n.02').definition())

# 특별히 원하는 품사의 Synset만 따로 추출해 사용(lead의 Synset 중 품사가 명사인 경우만 추출)
synsets = wn.synsets('lead', 'n')
print(synsets)

# 단어의 품사에 따라 감성 지수는 달라진다.
# 감성 지수를 정확하게 계산하려면 원하는 품사의 Synset을 정확히 지정해 사용해야한다.
