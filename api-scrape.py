import requests

html = requests.get('https://www.mixcloud.com/StereoLibre/')

data = html.json()

print(data['name'])
# soup = BeautifulSoup(html.text, 'html.parser')
# sections = soup.find_all('section',{'class':'card'})
