import re
import pickle as pkl

with open("tldCountsDataset/index.html","rb") as f:
	text = (f.read())
text = text.decode("utf-8")
text = (text.split())
i = 0
d = {}
l = {}
ext = ""
num = 0
for x in text:
	if(i%2):
		# print(int(x.replace(',', '').replace('N/A','0')))
		d[ext]=x.replace(',', '').replace('N/A','0')
		l[ext]=num
		num+=1
	else:
		ext = x
		# print(x,end=" ")
	i+=1
with open("counts.pkl","wb") as f:
	# pkl.while :
	# 	pass
	pkl.dump(l,f)
# print(l[".net"])
# pattern = ('class="selection"....')
# pattern = "."
# print(pattern)
# urls = (re.findall(pattern, text))
# for x in urls:
# 	print(x)