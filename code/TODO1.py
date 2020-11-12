import pandas as pd

dataset = pd.read_csv("C:/Users/ComputerGuy/Downloads/Compressed/top-1m.csv/top-1m.csv")
# with open("C:/Users/ComputerGuy/Downloads/Compressed/top-1m.csv/top-1m.csv","r") as f:
# 	print(f.read())
# print(dataset)
website = (dataset.loc[:,["website"]].values)
for x in website[:50]:
	print(x[0])
	Levenshtein.editops('LEAD','LAST')