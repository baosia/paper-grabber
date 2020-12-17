# PaperGrabber v2.1
# Based on code from https://predictablynoisy.com/scrape-biorxiv
# Please support the original author

#import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import cfscrape as cfs

# User Specific inputs:
# Starting Year (20XX format)
yrStart = 2020
# Ending year
yrEnd = 2020
# Starting month
mnStart = 11
# Ending month
mnEnd = 12
# Starting day
dayStart = 15
# Ending day
dayEnd = 15
# Collection code from bioRxiv
collection_code = "Cell Biology"
# output path and filename (for windows!)
#fileOut = r"C:\Users\hawkid\Desktop\bRx"+collection_code+str(mn)+str(yr)+r".csv"
fileOut = r"C:\Users\betho\Desktop\bRx"+collection_code+str(mnStart)+str(dayStart)+str(yrStart)+r".csv"

# Create URL for search query
cc = collection_code.replace(" ", "%20")
urlBase = "https://www.biorxiv.org/search/jcode%3Abiorxiv%20subject_collection_code%3A{}".format(cc)
urlDelta = "%20limit_from%3A{0}-{1}-{2}%20limit_to%3A{3}-{4}-{5}%20numresults%3A1000%20sort%3Apublication-date%20direction%3Aascending%20format_result%3Astandard"
url = urlBase + urlDelta

# initialize list
all_articles = []

# spoof browser headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}

# Populate the fields with current query and "get" it
query_url = url.format(yrStart, mnStart, dayStart, yrEnd, mnEnd, dayEnd)

#deal with cloudflair ddos protection splash.
scraper = cfs.create_scraper()
cfavoid = scraper.get(query_url, headers=headers)
#resq = requests.get(query_url, headers=headers)
#print(cfavoid)
html = bs(cfavoid.text)
#print(query_url)
#print(resp)
#print(html)

# Collect the articles in a list
articles = html.find_all('li', attrs={'class': 'search-result'})
print(articles)
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

    #assign collumn
    person = 'member'

    # Collect all year / month / title / author / link information
    all_articles.append([person, yrStart, mnStart, title, all_authors2, hyperlink])

# Put into dataframes and write to a csv
articles = pd.DataFrame(all_articles, columns=['Team Member', 'year', 'month', 'title', 'authors', 'link'])
print(articles)

# export to csv
articles_csv = articles.to_csv(fileOut, index=None, header=True)

#from pathlib import Path, PureWindowsPath
#csv_path = Path("/cygdrive/c/Users/bosia/Desktop/")
#csv_name = 'biorxiv.csv'
#winPath = PureWindowsPath(csv_path)
#articles_csv = articles.to_csv(str(winPath)+str(csv_name), index=None, header=True)

