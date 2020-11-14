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
import numpy as np
from sklearn.feature_extraction import FeatureHasher
hasher = FeatureHasher(n_features=5)
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
stopwords = (set(stopwords.words('english')))
words = open("Snippets/words-by-frequency.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)
with open("./feed.txt","r") as f:
	url_list = f.read().split()
verified_online = pd.read_csv("./verified_online.csv")
verfied_online_urls = verified_online.loc[:,"url"].values
with open("./Snippets/counts.pkl","rb") as f:
	tld_data = pkl.load(f)
dataset = pd.read_csv("./top-1m.csv")
website = (dataset.loc[:,["website"]].values)
def readCybercrimes():
	urls = []
	with open("./CYBERCRiME-11-12-20.txt","rb") as f:
		g = f.readlines()
	for h in g:
		urls.append(h.decode("utf-8").replace("\n",""))
	return urls
url_list.extend(readCybercrimes())
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
def edit_distance_list(url,topN=300):
	o = urlparse(url)
	ext = (tldextract.extract(o.netloc))
	url_ext = ext.subdomain+(ext.domain)
	
	features = []
	global minx
	global mina
	mina = 99999999
	minx = 0
	for x in website[:topN]:
		comp = urlsimpler(x[0])
		compo = urlparse(comp)
		comp_ext = (tldextract.extract(compo.netloc))
		comp_domain = comp_ext.domain
		ed = Levenshtein.editops(url_ext,comp_domain)
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
		weight = insert+replace+delete
		if(weight<mina):
			mina = weight
			minx = x
		features.extend([insert,replace,delete])
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
	try:
		domain = whois.query(url_extinct)
	except UnicodeDecodeError:
		return ["null","null","null"]
	
	if(domain!=None):
		domain = domain.__dict__
		ls = (list(domain.get("name_servers")))
		try:
			return [domain.get("registrar"),fixWord(ls[0]),fixWord(ls[1])]
		except:
			return ["null","null","null"]
	return ["null","null","null"]
def encoding(url):
	u = getGoogleFormat(url)
	out = [ord(x) for x in u]
	padding = [0 for x in range(253-len(out))]
	out.extend(padding)
	return out
def getIndex(extension):
	global tld_data
	try:
		return (tld_data[extension])
	except KeyError:
		return 0
def getTLDindex(url):
	o = urlparse(url)
	url_ext = ((tldextract.extract(o.netloc)))
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
	return len(re.findall("[0-9]", url_extinct))
def readPKL(file):
	with open(file,"rb") as f:
		ret = pkl.load(f)
	return ret
def getFromDict(dic,val):
	try:
		ret = dic[val]
	except KeyError:
		return 0
	return ret
cun = readPKL("cunFinal.pkl")
i = 0
url_list.extend(verfied_online_urls)
print(len(url_list))
all_data = []
for url in url_list:
	url,http,www = urlsimpler(url,returnMetadata=True)
	edl = ((edit_distance_list(url)))
	words = (url_to_words(url))
	whoisa_arr = None
	whoisnameserver_arr = None
	whoisa_dict = {}
	whoisnameserver_dict = {}
	try:
		whoises = (whoIs(url))
		whoisa_dict[whoises[0]] = getFromDict(cun["whoisa"],whoises[0])/693
		whoisnameserver_dict[whoises[1]] = getFromDict(cun["whoisnameserver"],whoises[1])/191
		whoisnameserver_dict[whoises[2]] = getFromDict(cun["whoisnameserver"],whoises[2])/191
	except whois.exceptions.UnknownTld:
		pass
	
	whoisa_arr = hasher.transform([whoisa_dict]).toarray()
	whoisa_arr = whoisa_arr.tolist()
	whoisnameserver_arr = hasher.transform([whoisnameserver_dict]).toarray()
	whoisnameserver_arr = whoisnameserver_arr.tolist()
	enc = (encoding(url))
	enc_array = (enc)
	tldIndex = [(getTLDindex(url))]
	hw = [http,www]
	url_sentence = (" ".join(words))
	url_sentence = (nlpized(url_sentence))
	uNLP_array = None
	uNLP_dict = {}
	for word in url_sentence:
		uNLP_dict[word] = getFromDict(cun["uNLP"],word)
	uNLP_array = hasher.transform([uNLP_dict]).toarray()
	uNLP_array = uNLP_array.tolist()
	countDigit = [(countDigits(url))]
	o = urlparse(url)
	wordz = ([x for x in nlpized(" ".join(o.path.split("/")))])
	sNLP_array = None
	sNLP_dict = {}
	for word in wordz:
		if not word:
			continue
		sNLP_dict[word] = getFromDict(cun["sNLP"],word)
	sNLP_array = hasher.transform([sNLP_dict]).toarray()
	sNLP_array = sNLP_array.tolist()
	features = whoisa_arr[0] #hashed
	features.extend(edl) #simple array
	features.extend(whoisnameserver_arr[0]) #hashed
	features.extend(enc_array) #256
	features.extend(tldIndex) #1
	features.extend(hw) #2
	features.extend(uNLP_array[0]) #hashed
	features.extend(sNLP_array[0]) #hashed
	features.extend(countDigit) #hase
	all_data.append(features)
	i+=1
	if(i%100==99):
		print(i)
		with open("features.pkl","wb") as f:
			pkl.dump(all_data, f)
with open("featuresFinal.pkl","wb") as f:
	pkl.dump(all_data, f)