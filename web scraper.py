from bs4 import BeautifulSoup
import requests
url=requests.get("https://edition.cnn.com/2024/11/13/middleeast/israel-expands-ground-operation-lebanon-intl-latam/index.html")
soup = BeautifulSoup(url.text,'html.parser')

title = soup.find("h1").text
paragraphs=[]
paragraphs.append(soup.find_all("p").text)
paragraph=""
for p in soup.find_all("p", href=False):
    paragraph=paragraph + p.get_text()

print(title)
print (paragraph)
