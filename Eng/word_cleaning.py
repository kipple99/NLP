from text import TEXT
import nltk
from text import TEXT
from nltk.tokenize import word_tokenize
nltk.download('punkt')
from collections import Counter

corpus = TEXT
print(corpus)

# 해당 본문에서 등장 빈도가 2 이하인 단어들만 찾아보기

# 전체 단어 토큰 리스트
# 빈도수 계산을 위해선 먼저 코퍼스를 단어 기준으로 토큰화
tokenized_words = word_tokenize(corpus)

# 파이썬의 Counter 모듈을 통해 단어의 빈도수를 카운트하여 단어 집합 생성
# 단어의 등장 빈도를 Counter() 함수로 계산
# Counter()는 파라미터로 단어 리스트를 받고, 각 단어의 등장 빈도를 딕셔너리 형태로 반환
vocab = Counter(tokenized_words)

# 빈도수가 2 이하인 단어리스트 추출
# list comprehension 문법 사용
uncommon_words = [key for key, value in vocab.items() if value <= 2]

# 빈도수가 2 이하인 단어들만 제거한 결과를 따로 저장
cleand_by_freq = [word for word in tokenized_words if word not in uncommon_words]

print('빈도수가 3이상인 토큰 수:', len(cleand_by_freq))

# 길이가 짧은 단어(영어 단어의 경우, 알파벳 하나 또는 두개로 구성된 단어는 줒요하지 않을 가능성이 높음)

# 길이가 2 이하인 단어 제거
cleand_by_freq_len = []

for word in cleand_by_freq:
    if len(word) > 2:
        cleand_by_freq_len.append(word)
        

# 콤마, to, on, I 등 큰의미를 갖지 않는 단어들이 잘 제거됨
print('정제 전:', cleand_by_freq[:10])
print('정제 후:', cleand_by_freq_len[:10])
