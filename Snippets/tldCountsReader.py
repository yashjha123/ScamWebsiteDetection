import pickle as pkl
with open("counts.pkl","rb") as f:
	tld_data = pkl.load(f)
# print(tld_data)
def getIndex(extension):
	global tld_data
	print(tld_data[extension])
getIndex(".net")