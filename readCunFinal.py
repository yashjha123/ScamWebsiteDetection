from matplotlib import pyplot as plt
import numpy as np
import pickle as pkl
from sklearn.preprocessing import OneHotEncoder
with open("cunFinal.pkl","rb") as f:
	cun = pkl.load(f)
whois = (cun["whoisa"])
# print(whois)
l = []
for x in whois:
	a = (x,whois[x])
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
	if x[1]>5:
		bars.append([x[0]])
	# print(x)
whoisa = OneHotEncoder()
whoisa.fit(bars)
print(whoisa.categories_)
print(whoisa.transform([["NameWeb BVBA"]]).toarray())
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