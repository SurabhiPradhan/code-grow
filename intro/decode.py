import requests
from bs4 import BeautifulSoup

base_url = 'https://timesofindia.indiatimes.com/'
r = requests.get(base_url)
soup = BeautifulSoup(r.content, "html.parser")

for heading in soup.findAll("h2", class_="hd1"):
    print('\n', heading.text,'\n')


