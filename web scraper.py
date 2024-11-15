from bs4 import BeautifulSoup
soup = BeautifulSoup("https://edition.cnn.com/world",'html.parser')
print(soup)