import nltk
from  nltk.tokenize import word_tokenize

nltk.download('punkt')
# punkt는 마침표나 약어(Mr. , Dr.)와 같은 특별한 언어적 특성을 고려하여 토큰화를 할 수 있게해주는 모듈이다.

#BTS - Dynamite
lyrics = "Cause I-I-I'm in the stars tonight, So watch me bring the fire and set the night alight"

# 단어 토큰화
tokenized_word = word_tokenize(lyrics)

print(tokenized_word)
