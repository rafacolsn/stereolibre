import requests
from bs4 import BeautifulSoup


html = requests.get('https://www.mixcloud.com/StereoLibre/')
soup = BeautifulSoup(html.text, 'html.parser')
sections = soup.find_all('section',{'class':'card'})

datas= {}
pubDate = ""

for section in sections:
    stats = []
    for a in section.find_all('a', {'class': 'album-art'}):
        for h1 in section.find_all('h1'):
            for dl in section.find_all('dl', {'class': 'card-stats'}):
                for dd in dl.find_all('dd'):
                    stats.append(dd.text)
                    datas[h1.text] = [a.get('href'), stats]


# print(len(datas))
            
