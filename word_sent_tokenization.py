import nltk
import pandas as pd
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

text = "My email address is 'abcde@example.com'. Send it to Mr.Kuk."

# 문장 토큰화
tokenized_sents = sent_tokenize(text)

# 결과 확인
print(tokenized_sents)
# 마침표를 기준으로 나눴지만 abcde@example.com에 .은 punkt 모듈로 인해 언어적 특성을 고려해 문장 토큰화가 되었다.

text = 'Can you forward my email to Mr.Kuk? Thank you!'
tokenized_sents = sent_tokenize(text)
print(tokenized_sents)
