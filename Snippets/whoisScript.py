import whois
# print(whois)
domain = whois.query('google.com')
# print(domain)
f = (domain.__dict__)
print("{")
for x in f:
	print(end="   ")
	print('"',x,'"'," : ",f[x],sep="")
print("}")