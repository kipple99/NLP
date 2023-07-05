# 필요한 패키지와 함수 불러오기
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from text import TEXT

corpus = TEXT

# 여기에 문장 단위 토큰화 코드를 작성하세요
tokenized_sent = sent_tokenize(corpus)

# 테스트 코드
print(tokenized_sent)