import requests
import os
import bs4

os.makedirs('flickr')
category = input("Enter search criteria: ").replace(' ','+')
url = "https://www.flickr.com/search/?text=" + category
soup = bs4.BeautifulSoup(url.text,"html.parser")
count = 0

for link in soup.find_all('img'):
    picture_url = link.get('src')[2:]
    if picture_url[0] == 'i':
        count += 1
        picture_url = 'http://' + picture_url
        f = open('{0}.jpg'.format(count),'wb')
        f.write(requests.get(picture_url).content)
        f.close()

print('Done.')