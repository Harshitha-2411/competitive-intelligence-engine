import requests
from bs4 import BeautifulSoup
from config import HEADERS

def scrape(url):

    try:

        r = requests.get(
            url,
            headers=HEADERS,
            timeout=20
        )

        soup = BeautifulSoup(r.text, "html.parser")

        title = soup.title.text.strip() if soup.title else ""

        description = ""

        meta = soup.find("meta", attrs={"name":"description"})

        if meta:
            description = meta.get("content","")

        h1 = ""

        if soup.find("h1"):
            h1 = soup.find("h1").text.strip()

        return {
            "URL":url,
            "Title":title,
            "H1":h1,
            "Description":description,
            "Status":r.status_code
        }

    except Exception as e:

        return {
            "URL":url,
            "Title":"",
            "H1":"",
            "Description":"",
            "Status":"Error",
            "Error":str(e)
        }