import whois
import re
import pandas as pd
import tldextract
import Levenshtein
import tldextract
from urllib.parse import urlparse
from math import log
import pickle as pkl
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import OneHotEncoder
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
stopwords = (set(stopwords.words('english')))

words = open("Snippets/words-by-frequency.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)
"""
Input Features Scheme
1) ED Sub domain + Domain cs.ml		5000
2) ED Subpage /admin/index.html		5000
3) Encoding sub pages 				100(expected) or 0
4) URL to Words 					200 words max
5) whoIs 							100 words max
6) Encoding							67 words max
7) tldCount							1
8) HTTP and WWW 					2
9) NLP Preprocessing				10
10) No. of digits 					1
11) NLP in Subpages 				100(expected)
"""

with open("./Dataset/feed.txt","r") as f:
	url_list = f.read().split()
with open("./Snippets/counts.pkl","rb") as f:
	tld_data = pkl.load(f)
dataset = pd.read_csv("C:/Users/ComputerGuy/Downloads/Compressed/top-1m.csv/top-1m.csv")
website = (dataset.loc[:,["website"]].values)
# url_list = ["whitetms.com/loader/"]
## to get google.com domain+suffix
def infer_spaces(s):
	def best_match(i):
		candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
		
		return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)
	cost = [0]
	for i in range(1,len(s)+1):
		c,k = best_match(i)
		cost.append(c)
	out = []
	i = len(s)
	f = ""
	while i>0:
		c,k = best_match(i)
		assert c == cost[i]
		if(i-i+k)==1:
			f=s[i-k:i]+f
		else:
			if(f!=""):
				out.append(f)
			f=""
			out.append(s[i-k:i])
		i -= k
	if(f!=""):
		out.append(f)
	voh = "^".join(reversed(out))
	return voh.split("^")
def urlsimpler(url,returnMetadata=False):
	urlS = 0
	p = 0
	http = -1
	if(url.startswith("https://")):
		starter = "https://"
		http = 1
		p = 8
	elif(url.startswith("http://")):
		starter = "http://"
		http = 2
		p = 7
	else:
		starter = "https://"
		http = 1
	url = url[p:]
	www = 0
	if(url.startswith("www3.")):
		w3 = ""
		www = 2
		url = url[4:]
	elif(url.startswith("www.")):
		www = 1
		url = url[3:]
	else:
		www = 1
		w3 = "www."
	if(returnMetadata==True):
		return (starter+url),http,www
	return starter+url
def edit_distance_list(url,topN=10000):
	o = urlparse(url)
	ext = (tldextract.extract(o.netloc))
	# print(ext)
	# continue
	url_ext = ext.subdomain+(ext.domain)
	print(url_ext,end=" ")
	
	features = []
	global minx
	global mina
	mina = 99999999
	minx = 0
	for x in website[:topN]:
		# print(x[0])
		# print(url_ext,".".join(x[0].split(".")[:-1]))
		comp = urlsimpler(x[0])
		compo = urlparse(comp)
		comp_ext = (tldextract.extract(compo.netloc))
		comp_domain = comp_ext.domain
		# print(comp_domain)
		ed = Levenshtein.editops(url_ext,comp_domain)
		# print(ed)
		insert = 0
		replace = 0
		delete = 0
		for g in ed:
			if(g[0]=="insert"):
				insert+=1
			if(g[0]=="replace"):
				replace+=1
			if(g[0]=="delete"):
				delete+=1
		# print(insert*2,replace*5,delete)
		weight = insert+replace+delete
		if(weight<mina):
			mina = weight
			minx = x
		features.append([insert,replace,delete])
	return features
def url_to_words(url):
	o = urlparse(url)
	ext = (tldextract.extract(o.netloc))
	url_ext = ext.subdomain+(ext.domain)
	return (infer_spaces(url_ext.replace(".","")))
def getGoogleFormat(url):
	o = urlparse(url)
	url_ext = ((tldextract.extract(o.netloc)))
	url_extinct = url_ext.domain+"."+url_ext.suffix
	return url_extinct
def fixWord(word):

	return word.replace("\n","").replace("\r","")
def whoIs(url):
	o = urlparse(url)
	url_ext = ((tldextract.extract(o.netloc)))
	url_extinct = url_ext.domain+"."+url_ext.suffix
	# url_extinct = "google.com"
	domain = whois.query(url_extinct)
	# print(url_extinct)
	
	if(domain!=None):
		domain = domain.__dict__
		ls = (list(domain.get("name_servers")))
		return [domain.get("registrar"),fixWord(ls[0]),fixWord(ls[1])]
	return ["null","null","null"]
def encoding(url):
	u = getGoogleFormat(url)
	out = [ord(x) for x in u]
	return out
def getIndex(extension):
	global tld_data
	try:
		return (tld_data[extension])
	except KeyError:
		return "N/A"
def getTLDindex(url):
	o = urlparse(url)
	url_ext = ((tldextract.extract(o.netloc)))
	# url_extinct = url_ext.domain+"."+url_ext.suffix
	return getIndex("."+url_ext.suffix)
def nlpized(text):
	no_special_char=[]
	for sentence in text:
		no_special_char.append(re.sub('[^A-Za-z0-9 ]+', '', sentence))
	spc = ("".join(no_special_char))
	no_special_char = spc.split(" ")
	no_stopwords = []
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
	return lemmatized
def countDigits(url):
	o = urlparse(url)
	url_ext = ((tldextract.extract(o.netloc)))
	url_extinct = url_ext.subdomain+url_ext.domain
	# print(url_extinct)
	return len(re.findall("[0-9]", url_extinct))

for url in url_list:
	url,http,www = urlsimpler(url,returnMetadata=True)
	# Edit Distance List
	print((edit_distance_list(url)))
	
	print(minx[0])
	# url to words then to NLP so donot count this	
	words = (url_to_words(url))
	print(words)
	# whois
	try:
		print(whoIs(url))
	except whois.exceptions.UnknownTld:
		print("Doesnot Exists")
	# Text to ASCII
	print(encoding(url))
	# TLD Counts
	print(getTLDindex(url))
	#http or https, www or www3
	print(http,www)
	#NLP
	url_sentence = (" ".join(words))
	print(nlpized(url_sentence))
	#Count the no. of digits
	print(countDigits(url))
	# Subpages
	o = urlparse(url)
	print([nlpized(x) for x in o.path.split("/")])