import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from processing import pos_tagger
from processing import penn_to_wn
from text import TEXT
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

corpus = TEXT
tokenized_sents = sent_tokenize(corpus)
pos_tagged_words = pos_tagger(tokenized_sents)

lemmatizer = WordNetLemmatizer()

# 표제어 추출 함수
def words_lemmatizer(pos_tagged_words):
    lemmatized_words = []
    
    # 여기에 코드를 작성하세요.
    for word, tag in pos_tagged_words:
        wn_tag = penn_to_wn(tag)
        
        if wn_tag in (wn.NOUN, wn.ADJ, wn.ADV, wn.VERB):
            lemmatized_words.append(lemmatizer.lemmatize(word, wn_tag))
        else:
            lemmatized_words.append(word)
            
    return lemmatized_words
    
words_lemmatizer(pos_tagged_words)