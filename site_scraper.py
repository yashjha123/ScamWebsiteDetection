import requests
import re
import pickle as pkl

s = requests.Session()

def getPage(page):
	global s
	r = s.get("https://db.aa419.org/fakebankslist.php?start="+page)
	# print(r.text)

	txt = r.text
	# txt = txt.replace("\n","")
	# print(txt)
	txt = txt.replace("\n","")
	# print(txt)
	# quit()
	sites = re.findall('\<table class="ewTable" summary="A list of currently known fake banks."\>(.+)\</table\>',txt)[0]	
	# sites = '<tr class="ewTableRow"><td><a href="fakebanksview.php?key=146823"><span class="phpmaker"><img src=\'images/browse.gif\' alt=\'View\' width=\'16\' height=\'16\' border=\'0\' /></span></a></td><td id="domainname146823"><a href="https://www.euro-transports.co.uk" rel="nofollow" target="_blank">https://www.euro-transports.co.uk</a>&nbsp;</td><td>Euro Transporter&nbsp;</td><td id="domainstatus146823" style="background-color: rgba(255,0,0,0.15);">active&nbsp;</td><td>2020-11-03 23:37&nbsp;</td><td>2020-11-03 23:37&nbsp;</td><td></td></tr><tr class="ewTableAltRow"><td><a href="fakebanksview.php?key=146822"><span class="phpmaker"><img src=\'images/browse.gif\' alt=\'View\' width=\'16\' height=\'16\' border=\'0\' /></span></a></td><td id="domainname146822"><a href="https://www.unilogshipment.com" rel="nofollow" target="_blank">https://www.unilogshipment.com</a>&nbsp;</td><td>United Logistics Shipment&nbsp;</td><td id="domainstatus146822" style="background-color: rgba(255,0,0,0.15);">active&nbsp;</td><td>2020-11-03 23:24&nbsp;</td><td>2020-11-03 23:24&nbsp;</td><td></td></tr>'

	# sites = '<tr class="ewTableRow">123</tr><tr class="ewTableRow">123</tr>'
	sites = sites.replace("ewTableAltRow","ewTableRow")
	names = re.findall('\<tr class="ewTableRow"\>(.+?)\</tr\>',sites)
	ret = []
	for x in names:
		a = {}
		try:
			a["code"]=(re.findall('\<a href="(.+?)"\>',x)[0]) #Specific Code
			a["url"]=(re.findall('target="_blank"\>(.+?)\</a>',x)[0]) #URL
			a["siteName"]=(re.findall('\</a\>&nbsp\;\</td\>\<td\>(.+?)&nbsp\;\</td\>',x)[0]) #Site Name
			a["status"]=(re.findall('\)\;"\>(.+?)&nbsp\;\</td\>',x)[0]) #Status
		except:
			pass
		ret.append(a)
	return ret
# for x in names:
# 	print()
l = []
for x in range(1,145155,20):
	l.extend(getPage(str(x)))
# print(l)
with open("file.pkl","wb") as f:
	pkl.dump(l,f)
