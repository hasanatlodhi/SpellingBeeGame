import bs4
import requests


URL = "https://www.3plearning.com/blog/spelling-bee-words-list/"
r = requests.get(URL)

soup=bs4.BeautifulSoup(r.content,'lxml')
soup.prettify()

mydivs = soup.find("tbody", {"class": "row-hover"})

tablerows=mydivs.find_all("tr")
with open(file='words.txt', mode='a') as file:
    for i in tablerows:
        classname = i.find(class_='column-1')
        file.write(f'\n{classname.text}')
