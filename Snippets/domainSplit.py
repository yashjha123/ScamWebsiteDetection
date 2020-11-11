import tldextract
from urllib.parse import urlparse
from urllib.parse import unquote

o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html?a=123')
# print(o)
print(o.scheme)
# print(o.netloc.split("."))
ext = (tldextract.extract(o.netloc))
print(ext.subdomain)
print(ext.domain)
print(ext.suffix)
print(unquote(o.path))
print(o.params)
print(o.query)