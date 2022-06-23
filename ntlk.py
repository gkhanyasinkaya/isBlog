import null as null
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import nltk

#f = open("output.txt", "r")
#f1 = open("output", "r")
#text = f.read()
#inputText = "Find new ideas and classic advice on strategy  innovation and leadership  for global leaders from the world s best business and management experts"

stop_words = set(stopwords.words('english')) # içeri alınabilir
total=843

def parserNormal(text):
  text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
  words = text.split()
  lemmed = [WordNetLemmatizer().lemmatize(w) for w in words]
  lemmed = [w for w in lemmed if not w in stop_words]
  firstList = []
  for i in lemmed:
    new_word = [i,0]
    firstList.append(new_word)
    for j in lemmed:
      if i == j:
        lemmed.remove(j)
        new_word[1] += 1
  #print(firstList)
  return firstList

def parserTagged(text):
  tokenized = sent_tokenize(text)
  for i in tokenized:
    wordsList = nltk.word_tokenize(i)
    wordsList = [w for w in wordsList if not w in stop_words]
    tagged = nltk.pos_tag(wordsList)
  lastList = []
  for i in tagged:
    new_word = [i[0],i[1],0]
    lastList.append(new_word)
    for j in tagged:
      if i == j:
        tagged.remove(j)
        new_word[2] += 1
  #print(lastList)
  return (lastList)

def normalPoint(inputText,dataText):
  point = 0
  for i in inputText:
    for j in dataText:
      if i[0] == j[0]:
        point += i[1]*(j[1]/(total+1))
  point = (point / len(inputText)) * 100
  #print(point)
  return(point)

def taggedPoint(inputText,dataText):
  point = 0
  for i in inputText:
    for j in dataText:
      if i[0] == j[0]:
        point += i[2]*(j[2]/(total+1))
        if j[1][:2] == "VB":            #verb
          point = point * 2
        elif j[1][:2] == "NN":          #noun
          point = point * 1.25
        elif j[1][:2] == "JJ":          #adjective
          point = point * 1.50

  point = (point / len(inputText)) * 100
  #print(point)
  return(point)

def totalPoint(p1,p2):
  pLast = p1+p2
  if pLast>=10:
    return(10)
  else:
    return float("%.1f" % pLast)



#count = 0
#total = 0
#while count<50:
#  lines = f1.readline()
#  if lines != null:
#    count+=1
#    a = function1(lines)
#    b = function1(text)
#    p1 = function3(a,b)
#    a = function2(lines)
#    b = function2(text)
#    p2 = function4(a,b)
#    print(function5(p1,p2))
#    total += function5(p1,p2)