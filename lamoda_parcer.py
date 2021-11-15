import requests
from bs4 import BeautifulSoup as BS
import urllib.request
import re


link = "https://www.lamoda.ru/c/2478/clothes-futbolki/?page=1"
url = urllib.request.urlopen(link)
content = url.read()
soup = BS(content)
links =  [a['href'] for a in soup.find_all('a',href=re.compile('https.*\.jpg'))]
imgs = [img['src'] for img in soup.find_all('img', src=lambda x: x.endswith('.jpg'))]
new_links = []
links += imgs
new_links = []
for a in links:
    a = "http://" + a
    new_links.append(a)

print (len(new_links))
print("\n".join(new_links))

#for link in new_links:
  #  url = link
#filename = url.split('/')[-1]
#r = requests.get(url, allow_redirects=True)
#open(filename, 'wb').write(r.content)

