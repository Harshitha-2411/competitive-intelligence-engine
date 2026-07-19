import pandas as pd

from scraper import scrape
from config import URLS
from utils import save_csv

rows=[]

for url in URLS:

    print(url)

    rows.append(scrape(url))

df=pd.DataFrame(rows)

print(df)

save_csv(df,"website_info.csv")