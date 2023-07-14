import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
nltk.download('stopwords')
stopwords_set = set(stopwords.words('english'))

# 특정한 단어의 핵심이 되는 부분(어간:Stem) 추출

# NLTK 어간 추출(porterstemmer)
from nltk.stem import PorterStemmer

porter_stemmer = PorterStemmer()
text = 'You are so lovely, I am loving you now.'
porter_stemmer_word = []

# 단어 토큰화
tokenized_words = nltk.word_tokenize(text)

# 포터 스테머의 어간 추출
# 토큰화 된 단어를 순회하며 어간을 추출 후 결과를 porter_stemmed_words에 추가
for word in tokenized_words:
    stem = porter_stemmer.stem(word)
    # 단어가 포터 스테머 알고리즘 기준에 포함되면 추출된 어간을 반환, 그렇지 않으면 원래 단어 반환
    porter_stemmer_word.append(stem)
    
print('어간 추출 전 :', tokenized_words)
print('포터 스테머의 어간 추출 후 :', porter_stemmer_word)

# NLTK 어간 추출(lancasterstemmer)

from nltk.stem import LancasterStemmer

lancaster_stemmer = LancasterStemmer()
text = "You are so lovely. I am loving you now."
lancaster_stemmed_words = []

# 랭커스터 스테머의 어간 추출
for word in tokenized_words:
    stem = lancaster_stemmer.stem(word)
    lancaster_stemmed_words.append(stem)
    
print('어간 추출 전 :', tokenized_words)
print('랭커스터 스테머의 어간 추출 후 :', lancaster_stemmed_words)
