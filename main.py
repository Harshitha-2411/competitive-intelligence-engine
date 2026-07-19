import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article")

first_book = books[0]

title = first_book.h3.a["title"]

print(title)