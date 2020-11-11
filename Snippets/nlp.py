from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# print(stopwords.words("english"))
stopwords = (set(stopwords.words('english')))
# stopwords = (", ".join(stopwords.words('english')))
# print(stopwords)

import re
no_special_char=[]
for sentence in "hooli or is it is an amazing app owned by network enterprises $%$%@@@@@123":
    no_special_char.append(re.sub('[^A-Za-z0-9 ]+', '', sentence))
spc = ("".join(no_special_char))
no_special_char = spc.split(" ")
no_stopwords = []
# print(no_special_char)
# print(stopwords)
for sentence in no_special_char:
    tr = (''.join(e.lower() for e in sentence.split() if e.lower() not in stopwords))
    if(tr==""): continue
    no_stopwords.append(tr)

def stem_words(text):
    return " ".join([stemmer.stem(word) for word in text.split()])

text_stemmed = [stem_words(x) for x in no_stopwords]

def lemmatize_words(text):
    return " ".join([lemmatizer.lemmatize(word) for word in text.split()])

lemmatized = [lemmatize_words(x) for x in text_stemmed]
# print(lemmatizer.lemmatize("tri"))
print(" ".join(lemmatized))