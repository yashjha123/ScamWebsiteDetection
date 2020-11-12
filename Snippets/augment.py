import re
urls = ["0009gmail.com","facebook.com","0004games.com"]
augmented = []

for x in urls:
	edited = "".join(re.findall("[a-z.]",x))
	digits = len(re.findall("[0-9]",x))
	if(edited!=x):
		augmented.append([edited,digits])
print(augmented)