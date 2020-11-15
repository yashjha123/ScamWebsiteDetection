from matplotlib import pyplot as plt
import numpy as np
import pickle as pkl
from sklearn.preprocessing import OneHotEncoder
with open("cunFinal.pkl","rb") as f:
	cun = pkl.load(f)
whois = (cun["whoisnameserver"])
print(whois)
# exit()
# 693
def getOHE(lab,limit,file):
	# print(whois)
	l = []
	for x in lab:
		a = (x,lab[x])
		l.append(a)	
	def second(b):
		return b[1]

	(l.sort(key=second,reverse=True))
	# print(len(l))
	# quit()
	xaxis = []
	bars = []
	for x in (l):
		# xaxis.append((x[1]))
		# bars.append(x[0])
		if x[1]>limit:
			bars.append([x[0]])
		print(x)
	return
	print(len(bars),len(l))
	# return
	whoisa = OneHotEncoder(handle_unknown="ignore")
	whoisa.fit(bars)
	# print(whoisa.categories_)
	# print(whoisa.transform([["NameWeb BVBA"]]).toarray())
	with open(file,"wb") as f:
		pkl.dump(whoisa, f)

# getOHE((cun["whoisa"]), 5, "registrar.pkl")
getOHE((cun["whoisnameserver"]), 5, "nameservers.pkl")
# getOHE((cun["uNLP"]), 23, "uNLP.pkl")
# getOHE((cun["sNLP"]), 7, "sNLP.pkl")
# getOHE((cun["whoisa"]), 5, "registrar.pkl")
# print(len(bars))
# print(bars)
# quit()
# fig,ax = plt.subplots(1,1)
# print(xaxis)
# a = np.array(xaxis)
# # print(ArithmeticError)
# ax.hist(a)
# y_pos = np.arange(len(bars))

# plt.xticks(y_pos, bars)

# plt.show()