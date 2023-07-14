import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
nltk.download('wordnet')
nltk.download('sentiwordnet')
nltk.download('omw-1.4')

def get_sentiment_score(word, pos):
    # 단어와 품사 태그를 기반으로 Synsets 구하기
    synsets = wn.synsets(word, pos)
    
    # Synsets의 첫 번째 요소의 이름으로 단일 SentiSynset 구하기
    synset = synsets[0]
    senti_synset = swn.senti_synset(synset.name())
    
    # SentiSynset의 긍정 지수, 부정 지수 구하기
    pos_score = senti_synset.pos_score()
    neg_score = senti_synset.neg_score()
    
    # 긍정 지수 - 부정 지수로 감성 지수 값 계산해 반환하기
    sentiment_score = pos_score - neg_score
    
    return sentiment_score

get_sentiment_score('love', wn.VERB)
