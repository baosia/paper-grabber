import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

collection_code = "Cancer%20Biology"
urlBase = "https://www.biorxiv.org/search/jcode%3Amedrxiv%7C%7Cbiorxiv%20subject_collection_code%3A{}".format(collection_code)
urlDelta = "%20limit_from%3A{0}-{1}-{2}%20limit_to%3A{0}-{1}-{3}%20numresults%3A500%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Astandard"
url = urlBase + urlDelta

all_articles = []
yr = 2019
mn = 10
dayStart = 1
dayEnd = 31

# Populate the fields with current query and post it
query_url = url.format(yr, mn, dayStart, dayEnd)
resp = requests.post(query_url)
html = bs(resp.text)

# Collect the articles in a list
articles = html.find_all('li', attrs={'class': 'search-result'})
for article in articles:
    # Pull the title, if it's empty then skip it
    title = article.find('span', attrs={'class': 'highwire-cite-title'})
    #if title is None:
        #continue
    title = title.text.strip()

    # Get all authors
    all_authors = []
    authors = article.find_all('span', attrs={'class': 'highwire-citation-author'})
    for author in authors:
        all_authors.append(author.text)
    all_authors2 = ', '.join(all_authors)
    # Get the first author's name
    #authors = article.find('span', attrs={'class': 'highwire-citation-author'})
    #author = authors.text.strip()

    # Get the link to the publication
    linkStrt = 'https://www.biorxiv.org'
    linkEnd = article.find('a')['href']
    link = linkStrt + linkEnd
    hyperlink = "=HYPERLINK(\"" + link + "\")"

    # Collect all year / month / title / author / link information
    all_articles.append([yr, mn, title, all_authors2, hyperlink])

# Put into dataframes and write to a csv
articles = pd.DataFrame(all_articles, columns=['year', 'month', 'title', 'authors', 'link'])
print(articles)

articles_csv = articles.to_csv(r'C:\Users\bosia\Desktop\bioRxiv.csv', index = None, header=True)

#from pathlib import Path, PureWindowsPath
#csv_path = Path("/cygdrive/c/Users/bosia/Desktop/")
#csv_name = 'biorxiv.csv'
#winPath = PureWindowsPath(csv_path)
#articles_csv = articles.to_csv(str(winPath)+str(csv_name), index=None, header=True)

