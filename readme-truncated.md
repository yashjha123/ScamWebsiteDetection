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

## ISP's Response after Detection
Once the ISP has detected whether the site that user has visited is fraud or not, they can redirect the response to a website thus warning the user/customer about the site he is going to visit.


## Detection from URL
AI cannot be used everywhere, so it won't be easy to do it on an ISP server. To do this, we have another model; in this case, the Random Forest Algorithm to indicate the frauds from a list of sites. Here is the list of input features of the algorithm.

---

---

## Input Feature Details
---
## TODO List
---
## Datasets
---
## Useful Links

---