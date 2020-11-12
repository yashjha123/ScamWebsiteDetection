# Scam Website Detection

Categorizing the website, whether it is a scam or not. There may be algorithms detecting whether the website is a fraud. In this case, we are using ISP side detection to detect whether the site is fake or not.

ISPs have access to
1) The URLs a user visits
2) The data record, which site I view most and how much time I spend on a site
3) IP Addresses
4) Your Mac Addresses
5) Softwares you download (From the software website, may not be clear in case of using big hosting services)

## Http Sites
ISPs do not have access to the site content the customer is visiting in case of Https sites. In contrast, the content of Http sites can be easily accessed. Old fishing websites can be detected using a query search, e.g. Site with a form asking for Credit Card Details can be easily matched with query searches/regex thus preventing the user from accessing the data of the site.

## Microsoft Scams
Most of the Microsoft scams are you sharing your screen and giving input access to scammers.
1) As the ISPs have a track of software we download, as most of the scams first let you download a screen sharing software, e.g. TeamViewer then move on to ZohoAssist, etc. when they have access.
2) With the above point, we can trigger an ML detection on the sites they recently visited, thus getting the fraud URL.
3) As the ISP has access to the IPs where the client/customer is sending and retrieving data. We can track the scammer; if its location seems near to some identified scams, we can trigger the scam. 

## Banking Scams
1) Banking scams are a high threat, as we have a track of the consumer's history, we can access the site content by requesting the URL separately. Accessing the URL every time may be difficult.
2) Pattern matching in the domains.
3) Tracing the history of a user which led him to a particular website can also be used.

## ISP's Response after Detection
Once the ISP has detected whether the site that user has visited is fraud or not, they can redirect the response to a website thus warning the user/customer about the site he is going to visit.


## Detection from URL
AI cannot be used everywhere, so it won't be easy to do it on an ISP server. To do this, we have another model; in this case, the Random Forest Algorithm to indicate the frauds from a list of sites. Here is the list of input features of the algorithm.

- [x] Relatable to few known sites 
- [x] Some word for, e.g. Banks, Lons...
- [x] Maximum possible words (breaking a URL into words)
- [x] Whoislookup
- [x] Letter Embeddings Eg. Jijhaj is 101231 (Using ASCII here)
- [x] .com or .net etc. (tld-counts)
- [x] Adding a split on . and / for subdomains, .com or .net ... and subpages. (last .com for domain extension)
- [x] http or https and www or www3
- [x] Text Preprocessing Normalizing, Stemming and Lemmatization.
- [x] Number of digits in a URL
- [ ] Keyboard Typos Eg. biik instead of book
<br \>
- [ ] Distance between repeated letters book is 2 and letter is o
- [ ] Converting text Eg. hell0 to hello
- [ ] Statistics of a website (Number of people who have visited it.) (Alexa API but expensive)

- [ ] ~~Again similar URL wit different domains like microsoft.com and microsofti.in~~
- [ ] ~~Repeated Characters~~

1) Using URL_to_words to convert the URL into words for classifier encoding
2) Using the dp code to get deletions, additions, etc. For eg. Microsoftonline and Microsoft

## Input Feature Details
Feature Name | Size | Type 
--- | --- | --- 
Edit Distance List | 10000 | Array
whois | 3 | OneHotEncoder
Text to ASCII | 67(max) | Array
TLD Count | 1 | Number
http or https, www or www3 | 2 | 2 Numbers
NLP on url words | 1000(max) | OneHotEncoder
Count the no. of digit | 1 | 1 Number
NLP on Subpages | 1000(max) | OneHotEncoder

## TODO List
- [x] Getting the Top-50 list with Alexa for MED
- [x] Augmentation (Remove Numbers along with specific characters)
- [x] Getting the dataset (Phishing List)
- [ ] Comibining the snippets together
- [ ] Converting to input features of Random Forest Classifier

## Datasets
1) [Phishing site links, OpenPhish](https://openphish.com/feed.txt) 4305 sites
2) [Phishing site links, PhishTank](https://www.phishtank.com/developer_info.php) 14505 sites
3) [Phishing site links, CYBERCRiME](http://cybercrime-tracker.net/) 22470 sites
4) [Alex Top List](https://gist.github.com/chilts/7229605) [Download List as .zip](http://s3.amazonaws.com/alexa-static/top-1m.csv.zip)
5) [Using Majestic Million for non-phishing sites](http://cybercrime-tracker.net/)
6) [Rest of the Dataset, StopForumSpam](https://www.stopforumspam.com/downloads) 1000000 (unreliable, best not used)

## Useful Links

1) [Words from a URL](https://stackoverflow.com/questions/8870261/how-to-split-text-without-spaces-into-list-of-words)
2) [Useful repo](https://github.com/shramos/Awesome-Cybersecurity-Datasets)
3) [Reading .mat file](https://stackoverflow.com/questions/874461/read-mat-files-in-python)
4) [List of sites](https://lifars.com/wp-content/uploads/2016/11/Sites-with-blocklist-of-malicious-IPs-and-URLs.pdf)
5) Minimum Edit Distance with Paths [stackoverflow](https://stackoverflow.com/questions/10638597/minimum-edit-distance-reconstruction) [python package](https://pypi.org/project/python-Levenshtein/) [wheels](https://pypi.org/project/python-Levenshtein-wheels/)
6) Text Preprocessing [Medium Article](https://towardsdatascience.com/a-handbook-to-text-preprocessing-890f73fd28f8)