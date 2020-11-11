### Scam Website Detection

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

1) Relatable to few known sites
2) Some word for, e.g. Banks, Lons...
3) Repeated Characters
4) Converting text Eg. hell0 to hello
5) Maximum possible words
6) Statistics of a website (Number of people who have visited it.)
7) Distance between repeated letters book is 2 and letter is o
8) Letter Embeddings Eg. Jijhaj is 101231
9) .com or .net etc.
10) Again similar URL with different domains like microsoft.com and microsofti.in 


1) Using URL_to_words to convert the URL into words for classifier encoding
2) Using the dp code to get deletions, additions, etc. For eg. Microsoftonline and Microsoft

## Datasets
1) [Phishing site links, OpenPhish](https://openphish.com/feed.txt)
2) [Phishing site links, PhishTank](https://www.phishtank.com/developer_info.php)

## Useful Links
1) [Words from a URL](https://stackoverflow.com/questions/8870261/how-to-split-text-without-spaces-into-list-of-words)
2) [Useful repo](https://github.com/shramos/Awesome-Cybersecurity-Datasets)
3) [Reading .mat file](https://stackoverflow.com/questions/874461/read-mat-files-in-python)