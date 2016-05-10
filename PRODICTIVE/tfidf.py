import nltk
import string
import operator
from collections import Counter
#
# def get_tokens():
#    with open('/home/davyx8/Downloads/data sets/lebowski/fargo.txt', 'r') as shakes:
#     text = shakes.read()
#     lowers = text.lower()
#     #remove the punctuation using the character deletion step of translate
#     no_punctuation = lowers.translate(None, string.punctuation)
#     tokens = nltk.word_tokenize(no_punctuation)
#     return tokens
#
# tokens = get_tokens()
# count = Counter(tokens)
#
# stopwords = ['a', 'the', 'of', 'at', 'it','and','i','in','is','on','his','he','you','we','to','with','out','are','that']
#
# filtered = [w for w in tokens if not w in stopwords]
# count = Counter(filtered)
# print count.most_common(100)
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

path = '/home/davyx8/Downloads/medical data'
token_dict = {}
stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return tokens
import xml.etree.ElementTree as ET


for subdir, dirs, files in os.walk(path):
    for file in files:
        file_path = subdir + os.path.sep + file
        shakes = open(file_path, 'r')
        text = shakes.read()
        lowers = text.lower()
        no_punctuation = lowers.translate(None, string.punctuation)
        token_dict[file] = no_punctuation

#this can take some time
tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')

tfs = tfidf.fit_transform(token_dict.values())
feature_names = tfidf.get_feature_names()
sortedx = {}



for filename in token_dict:
    print filename
    file = token_dict[filename]

    sortedx = {}
    response = tfidf.transform([file])
    for col in response.nonzero()[1]:
        sortedx[feature_names[col]] = tfs[0,col]
    sortedx2 = sorted(sortedx.items(), key=operator.itemgetter(1))
    f = open('medicalTFIDF/'+filename,"w")
    for item in sortedx2:
        f.write(str(item[0])+ '- ' +str(item[1])+'\n')
    f.close()
