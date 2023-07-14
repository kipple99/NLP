# 필요한 패키지와 함수 불러오기
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from text import TEXT
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
nltk.download('wordnet')
nltk.download('sentiwordnet')

# sentiwordnet은 wordnet과 유사한 영어 어휘 사전이다.
# 하지만 Synset별로 긍정지수, 부정지수, 객관성 지수를 할당해 준다는 차이가 있다.

print('wordnet-happy: ', wn.synsets('happy'))
print('sentiwordnet-happy: ', list(swn.senti_synsets('happy')))

# 긍정 감성 지수 함수: pos_score()
# 부정 감성 지수 함수: neg_score()
# 객관성 지수 함수(감성 지수와 반대되는 개념으로 단어가 얼마나 감성적 어조와 관계없는지 보여주는 수치): obj_score()

happy_sentisynsets = list(swn.senti_synsets('happy'))

pos_score = happy_sentisynsets[0].pos_score()
neg_score = happy_sentisynsets[0].neg_score()
obj_score = happy_sentisynsets[0].obj_score()

print(pos_score, neg_score, obj_score)

# 최종 감성 지수로는 긍정 지수에서 부정 지수를 뺀 값이 사용된다.
# -1에 가까우면 부정적 의미를, 0에 가까우면 중립적인 의미, 1에 가까우면 긍정적인 의미를 가진 단어로 해석

print(pos_score - neg_score)

# 특정 품사의 SentisynSet 찾기

# 단어가 어떤 품사로 사용됐는지에 따라 감성 지수의 결과도 달라진다.

adj_synsets = wn.synsets('hard', wn.ADJ)
adv_synsets = wn.synsets('hard', wn.ADV)

# 가장 보편적인 의미로 사용되는 첫번째 Synset을 가져와서 분석
adj_synset = adj_synsets[0]
adv_synset = adv_synsets[0]

# 해당 Synset의 '단어, 품사, 순번' 정보를 swn.senti_synset()의 파라미터로 넣어준다.
# Synset의 '단어, 품사, 순번' 정보를 찾는 데에는 name() 함수가 사용된다.

adj_senti_synset = swn.senti_synset(adj_synset.name())
adv_senti_synset = swn.senti_synset(adv_synset.name())

# 형용사 hard는 부정적인 의미로 나오지만, 부사인 hard는 중립적 의미

print(adj_senti_synset)
print(adv_senti_synset)
