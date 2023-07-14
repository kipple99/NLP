import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from text import TEXT
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

corpus = TEXT
# 문장 토큰화
tokenized_sents = sent_tokenize(corpus)

def pos_tagger(tokenized_sents):
    pos_tagged_words = []

    for sentence in tokenized_sents:
        # 여기에 코드를 작성하세요
        # 단어 토큰화
        tokenized_words = word_tokenize(sentence)
        
        # 품사 태깅
        pos_tagged = pos_tag(tokenized_words)
        pos_tagged_words.extend(pos_tagged)
        
    return pos_tagged_words

# 테스트 코드
pos_tagger(tokenized_sents)
