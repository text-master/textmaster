from bs4 import BeautifulSoup
import requests


URL = "https://techcrunch.com/page/%d"
file = open('techcrunch.txt', 'a')

# r  = requests.get("https://techcrunch.com/page/2")



for i in range(1, 3):
    r = requests.get(URL % i)
    soup = BeautifulSoup(r.text, 'lxml')
    for link in soup.select('.post-title a'):
        link = link.get('href')
        article = requests.get(link)
        article_soup = BeautifulSoup(article.text, 'lxml')
        text = article_soup.select('.article-entry')[0].text
        text = text.encode('utf-8').strip()
        file.write('\n')
        file.write(text)


