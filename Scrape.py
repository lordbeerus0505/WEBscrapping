'''


from newspaper import Article
url='http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'

article= Article(url)
article.download()
article.html #specify type of file
article.parse()
#print(article.html)
print("hello")
print(article.authors)
#print(article.text)
fh=open("Scrape.txt","w")
fh.write("Grabbing the news...\n")
fh.write(article.text)

fh.close()

import requests


import newspaper
url="https://www.nytimes.com/"
print('Articles found...')
article=Article(url)
fh=open("Articles.txt","w")
paper=newspaper.build('https://www.nytimes.com/')
for x in paper.article_urls():
    print("hello")
    print(x.url)
    fh.write(x.url)
fh.close()

print("----------------------------------")
for category in paper.category_urls():
    print(category)



from newspaper import Article
from newspaper import fulltext
url='http://cnn.com'
fh=open("Articles.txt","w")
fh.write("Getting the news\n")
paper= newspaper.build(url)
for x in paper.articles:
    article=Article(x.url)
    print(x.url)
   # print(article)
    article.download()
    article.html
   # print(article.html)
    article.parse()
    fh.write(article.text)
    fh.write("-------------------------------------------------") #end of article
    fh.write("\n\n\n")

fh.close()




import newspaper
cnn_paper =newspaper.build('http://cnn.com')

for article in cnn_paper.articles:
    print(article.url)

cnn_article=cnn_paper.articles[1]
cnn_article.download()
cnn_article.html
cnn_article.parse()
print(cnn_article.text)

'''




from bs4 import BeautifulSoup
from newspaper import Article
from urllib.request import Request,urlopen
import re

request=Request("http://ndtv.com")
html_page=urlopen(request)
soup = BeautifulSoup(html_page,"lxml")
links=[]
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    print(link.get('href'))
    links.append(link.get('href'))


fh = open("Articles.txt",'w')
for url in links:
    article=Article(url)
    article.download()
    article.html
    article.parse()
    fh.write(article.text)
    fh.write("\n\n\n\n----------------------------------------------------------\n")

fh.close()




