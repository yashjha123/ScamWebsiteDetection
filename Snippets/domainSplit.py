import tldextract
from urllib.parse import urlparse
from urllib.parse import unquote

# o = urlparse('http://www.fuck.cwi.nl:80/%7Eguido/Python.html?a=123')
o = urlparse('google.com')

# print(o)
# print(o.netloc.split("."))

print(o.scheme) #http
ext = (tldextract.extract(o.netloc))
print(o.netloc) # www.cwi.nl:80
print(ext.subdomain) #www
print(ext.domain) #cwi
print(ext.suffix) #nl
print(unquote(o.path)) #/~guido/Python.html
print(o.params) #
print(o.query) #a=123
print()
print(ext.domain+"."+ext.suffix)


