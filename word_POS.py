import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tag import pos_tag
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

# 품사 태깅(POS; Part Of Speech Tagging)
# 각 단어가 어떤 푼사로 쓰였는지 표시하는 작업

from nltk.tag import pos_tag

text = "Watching Time Chasers, it obvious that it was made by a bunch of friends. Maybe they were sitting around one day in film school and said, \"Hey, let\'s pool our money together and make a really bad movie!\" Or something like that."
pos_tagged_words = []

# 문장 토큰화
# 품사 태깅할 코퍼스를 문장 기준으로 토큰화
tokenized_sents = sent_tokenize(text)

# 토큰화 된 문장등을 순화하며 순차적으로 단어 토큰화와 품사 태깅 작업 진행
for sentence in tokenized_sents:
    # 단어 토큰화
    tokenized_words = word_tokenize(sentence)
    
    # 품사 태깅
    pos_tagged = pos_tag(tokenized_words)
    pos_tagged_words.extend(pos_tagged)
    
print(pos_tagged_words)