import re
with open("../Dataset/verified_online.xml","r") as f:
	urls = (re.findall("\<url\>(.+?)\</url>",f.read()))
print(len(urls))