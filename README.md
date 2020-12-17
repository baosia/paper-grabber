# paper-grabber
A python script to scrape papers by date from BioRxiv collections and output to a csv file

Python version: 3.x

Dependencies/Libraries: 
cfscrape, bs4 (for BeautifulSoup), and pandas.

bs4 and pandas are available in the defult repository (see: https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html for package installation instructions).
cfscrape must be added manually and is available from https://github.com/Anorov/cloudflare-scrape . Download the repository, unzip, and add it to your project directory. Follow the installation instructions in the README file to add the module to pycharm. You may also need to install node.js to make cfscrape work correctly.  

Output file path is formatted for Windows

Recommended usage:
I run this in Pycharm (https://www.jetbrains.com/pycharm/) and add/change parameters within the script directly (see commented user specific inputs). 
Dependencies can be installed in Pycharm before running. 
Works well when run on Windows. I haven't tested it with Mac or Linux. 
