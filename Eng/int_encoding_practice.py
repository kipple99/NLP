# 필요한 패키지와 함수 불러오기
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from text import TEXT
nltk.download('punkt')

word_to_idx = {} # 단어 별 인덱스 부여하기 위한 딕셔너리
i = 0
encoded_idx = [] # 각 토큰의 정수 인덱스를 부여하기 위한 리스트
corpus = TEXT

tokenized_words = word_tokenize(corpus)

# 단어의 빈도수를 계산하여 정렬하는 코드를 작성하세요
vocab = Counter(tokenized_words)
vocab = vocab.most_common()

for (word, frequency) in vocab:
    # 여기에 코드를 작성하세요
    i += 1
    word_to_idx[word] = i

for word in tokenized_words:
    # 여기에 코드를 작성하세요
    idx = word_to_idx[word]
    encoded_idx.append(idx)


# 테스트 코드
encoded_idx
