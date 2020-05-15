import requests
from bs4 import BeautifulSoup


base_url = 'https://www.thehindu.com/'
r = requests.get(base_url)
soup = BeautifulSoup(r.content, "html.parser")

with open('filename.txt', 'w') as open_file:
    for heading in soup.findAll("div", class_="story-card-news"):
        print (heading.h2.text)

