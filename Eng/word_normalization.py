import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
nltk.download('stopwords')
stopwords_set = set(stopwords.words('english'))

text = 'What can I do for you? Do your homework now'

# 소문자로 변환
print(text.lower())

# 동의어 사전

# 같은 의미를 가지는 단어들을 어떤 형태로 정규화할지 설정
# 기준이 정해졌다면 정규화 할 단어들을 딕셔너리 형태의 동의어 사전 생성
synonym_dict = {'US':'USA', 'U.S':'USA','Ummm':'Umm','Ummmm':'Umm'}
text = "She became a US citizen. Ummmm, I think, maybe and or."
normalized_words = []



# 단어 토큰화

# 문장을 단어 토큰화 후 토큰들을 순회하며 동의어 사전의 키에 해당 단어가 포함되는지 확인
# 포함된다면 정규화할 단어로 변경
tokenized_words = nltk.word_tokenize(text)

for word in tokenized_words:
    # 동의어 사전에 있는 단어라면, value에 해당하는 값으로 변환
    if word in synonym_dict.keys():
        word = synonym_dict[word]
        
    normalized_words.append(word)
    
# 결과 확인
print(normalized_words)
