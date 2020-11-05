### Scam Website Detection

Categorizing the website, whether it is a scam or not. There may be algorithms detecting whether the website is fraud. In this case we are using ISP side detection to detect whether the site is fake or not.

ISPs have access to
1) The URLs a user visits to
2) The data record, which site I view most and how much time I spend on a site
3) IP Addresses
4) Your Mac Addresses
5) Softwares you download (From the software website, may not be clear in case of using big hosting services)

## Http Sites
ISPs do not have access to the site content the customer is visiting in case of Https sites. Whereas content of Http sites can be easily accessed. Old fishing websites can be detected using a query search, for e.g. Site with a form asking for Credit Card Details can be easily matched with query searches/regex thus preventing the user from accesssing the data of the site.

## Microsoft Scams
Most of the microsoft scams are you sharing your screen and giving input access to scammers.
1) As the ISPs have track of softwares we download, as most of the scams first let you download a screen sharing software e.g. TeamViewer then move on to ZohoAssist, etc. when they have access.
2) With the above point, we can trigger an ML detection on the sites they recently visited, thus getting the fraud URL.
3) As the ISP has access to the IPs where the client/customer is sending and retrieving data. We can track the scammer, if its location seems near to some identified scams, we can trigger the scam. 

## Banking Scams
1) Banking scams are a high threat, as we have a track of the consumer's history we can access the site content by requesting the url seperatly. Accessing the url everytime may be difficult.
2) Pattern matching in the domains.
3) Tracing the history of a user which led him to a particular website can also used

## ISPs Response after Detection
Once the ISP has detected whether the site that user has visited is fraud or not, they can redirect the response to a website thus warning the user/customer about the site he is going to visit.