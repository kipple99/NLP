import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
# from text import TEXT
from nltk.corpus import stopwords
nltk.download('stopwords')
stopwords_set = set(stopwords.words('english'))

print('불용어 개수 :', len(stopwords_set))
print(stopwords_set)