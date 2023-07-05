import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from text import TEXT
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# 표제어 : 단어의 사전적 어원
# 표제어 추출 : 서로 다른 단어도 표제어가 같은 경우가 있기 때문에, 표제어를 기준으로 통합하면 단어가 정규화된다.

text = 'You are the happiest person.'
tokenized_words = word_tokenize(text)

# 품사 태그
tagged_words = pos_tag(tokenized_words)

# Penn Treebank POS Tag를 WordNet POS Tag의 4가지 태그로 손쉽게 바꾸기
def penn_to_wn(tag):
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('N'):
        return wn.NOUN
    elif tag.startswith('R'):
        return wn.ADV
    elif tag.startswith('V'):
        return wn.VERB
    else:
        return
    
# penn_to_wn()을 이용해서 품사를 WordNet POS Tag로 바꾸고 표제어 추출해보기
lemmatizer = WordNetLemmatizer()
lemmatized_words = []

for word, tag in tagged_words:
    # WordNet Pos Tag로 변환
    wn_tag = penn_to_wn(tag)
    
    # 품사를 기준으로 표제어 추출
    if wn_tag in (wn.NOUN, wn.ADJ, wn.ADV, wn.VERB):
        lemmatized_words.append(lemmatizer.lemmatize(word, wn_tag))
    else:
        lemmatized_words.append(word)
        
# 표제어 추출 확인
print('표제어 추출 전 :', tokenized_words)
print('표제어 추출 후 :', lemmatized_words)