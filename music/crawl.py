"""Web scraping and crawling.
BeautifulSoup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""

#%%
# Setup / Data

from bs4 import BeautifulSoup
from bs4.element import Tag

import requests

from util import utility
from settings import *

#%%
# Getting started

# The Website to work with, i.e. to scrape info from and crawl over it - Ultimate Classic Rock.
# The starting URL refers to articles about The Beatles.
start_url = 'https://ultimateclassicrock.com/search/?s=The%20Beatles'

# # Location of the chromedriver used to work with selenium and Chrome;
# # apparently not necessary if webdriver_manager is used
# chromedriver_location = r'C:\Users\Vladan\AppData\Local\Programs\Python\Python312\Scripts\chromedriver.exe'

#%%
# Create Response object from GET request, using requests.get(<url>, allow_redirects=False)
response = requests.get(start_url, allow_redirects=False)

#%%
# Get response text from Response object, using <response>.text
response_text = response.text
response_text

#%%
# Get BeautifulSoup object from response text, using BeautifulSoup(<response text>, 'html.parser')
soup = BeautifulSoup(response_text, 'html.parser')
soup


#%%
def get_soup(url: str) -> BeautifulSoup:
    """Returns BeautifulSoup object from the corresponding URL, passed as a string.
    Creates Response object from HTTP GET request, using requests.get(<url string>, allow_redirects=False),
    and then uses the text field of the Response object and the 'html.parser' to create the BeautifulSoup object.
    """

    # Create Response object from HTTP GET request; assume that no redirection is allowed (allow_redirects=False)
    response = requests.get(url, allow_redirects=False)
    # Get text from the Response object, using <response>.text
    response_text = response.text
    # Create and return the corresponding BeautifulSoup object from the response text; use features='html.parser'
    return BeautifulSoup(response_text, features='html.parser')


#%%
# Test get_soup(url)
soup = get_soup(start_url)
soup

#%%
# Save BeautifulSoup object to an HTML file,
# using <Path-file-object>.write_text(str(<BeautifulSoup object>), encoding='utf-8', errors='replace').
html_file = utility.get_data_dir() / 'soup.html'
html_file.write_text(str(soup), encoding='utf-8', errors='replace')

#%%
# Demonstrate <BeautifulSoup object>.find('<tag>'); e.g., find the first 'article' tag.
article = soup.find('article')
article
# next_tag = article.find_next('span')
next_tag = article.find_next()
next_tag

#%%
# Demonstrate <BeautifulSoup object>.find('<tag>').find('<nested tag>'); e.g., find the 'a' tag in an 'article' tag.
soup.find('article').find('a')

#%%
# Demonstrate getting a tag with specific attributes
# using <BeautifulSoup object>.find('<tag>', {'<attribute>': '<value>'});
# e.g., find a 'span' tag with the 'visually-hidden' attribute.
soup.find('span', {'class': 'visually-hidden'})

#%%
# Demonstrate getting values of tag attributes,
# e.g. <BeautifulSoup object>.find('<tag>').text for an 'a' tag and for a 'span' tag (e.g., class='visually-hidden').
# soup.find('a').text
soup.a.text
# soup.find('span', {'class': 'visually-hidden'})
soup.find('span', {'class': 'visually-hidden'}).text

#%%
# Demonstrate <BeautifulSoup object>.find_all(<tag>), e.g. for the 'article' tag; returns a ResultSet object.
articles = soup.find_all('article')
len(articles)
type(articles)
articles[0]

#%%
# The following lines demonstrate that getting the soup with requests.get() does not capture all tags
# (those filled with JavaScript, e.g. 'time'). That's when using selenium.webdriver is better.
articles[0].time

#%%
# Selenium version, needed for extracting the <time> tag info

# # Guidelines - a deprecated version
# # (still OK if the chromedriver.exe version downloaded does not make Chrome-version problems):
# # Before running the following line(s), make sure to download and unzip
# # THE LATEST version of chromedriver (i.e., the one compatible with your version of Chrome)
# # and put chromedriver.exe in the Scripts subfolder of your Python installation folder,
# # e.g. C:\Users\Vladan\AppData\Local\Programs\Python\Python312\Scripts.
# # The driver should be downloaded from https://chromedriver.chromium.org/downloads.
# # Then you need not provide the path of the driver, just run: driver = webdriver.Chrome().
# # Alternatively, you can put the downloaded driver at a desired folder, e.g.
# # M:\Vladan\Downloads\chromedriver.exe, and get the driver by running:
# # driver = webdriver.Chrome('M:\\Vladan\\Downloads\\chromedriver.exe')
# # (Adapted from https://stackoverflow.com/a/60062969/1899061.)
#
# from selenium import webdriver
# driver = webdriver.Chrome()

# Alternatively, you can put the downloaded driver at a desired folder, e.g.
# M:\Vladan\Downloads\chromedriver.exe, and get the driver by running:
# driver = webdriver.Chrome('M:\\Vladan\\Downloads\\chromedriver.exe')

# # Guidelines - a version from
# # https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python/69892580#69892580:
# # The approach based on using the Service object.
# # Before running the following line(s), make sure to download and unzip
# # THE LATEST version of chromedriver (i.e., the one compatible with your version of Chrome)
# # and put chromedriver.exe in the Scripts subfolder of your Python installation folder,
# # e.g. C:\Users\Vladan\AppData\Local\Programs\Python\Python312\Scripts.
# # The driver should be downloaded from https://chromedriver.chromium.org/downloads.
# # Create the required Service object explicitly, using the Service class constructor,
# # and pass the absolute path of the chromedriver.exe.
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# service = Service(r'C:\Users\Vladan\AppData\Local\Programs\Python\Python312\Scripts\chromedriver.exe')
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)

# Guidelines - a version from
# https://stackoverflow.com/a/69885677:
# The approach based on using the Service object, but skips the ChromeOptions() object.
# Before running the following line(s), make sure to download and unzip
# THE LATEST version of chromedriver (i.e., the one compatible with your version of Chrome)
# and put chromedriver.exe in the Scripts subfolder of your Python installation folder,
# e.g. C:\Users\Vladan\AppData\Local\Programs\Python\Python312\Scripts.
# The driver should be downloaded from https://chromedriver.chromium.org/downloads.
# Create the required Service object explicitly, using the Service class constructor,
# and pass the absolute path of the chromedriver.exe.

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# # service = Service(r'C:\Users\Vladan\AppData\Local\Programs\Python\Python312\Scripts\chromedriver.exe')
# service = Service(chromedriver_location)
# driver = webdriver.Chrome(service=service)

# Guidelines - a version from
# https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python/70099102#70099102:
# The approach based on using the Service object.
# Apparently, no need to download the driver, it gets downloaded by ChromeDriverManager.
# However, you need to install the webdriver-manager package beforehand.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
service=Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# # driver.get("https://www.google.com")

# Once any of these approaches to get the Chrome driver is made to work,
# the following two lines get the page source (the HTML code) and turn it into a BeautifulSoup object:

driver.get(start_url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
# print('soup created')

#%%
type(driver)

#%%
# Save BeautifulSoup object to an HTML file,
# using <Path-file-object>.write_text(str(<BeautifulSoup object>), encoding='utf-8', errors='replace').
html_file.write_text(str(soup), encoding='utf-8', errors='replace')


#%%
def get_soup_selenium(url: str) -> BeautifulSoup:
    """Returns BeautifulSoup object from the corresponding URL, passed as a string.
    Makes an HTTP GET request, using driver = webdriver.Chrome() from the selenium package and its driver.get(url).
    Then uses the page_source field of the driver object and the 'html.parser' to create and return the BeautifulSoup o.
    """
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    service=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(url)
    return BeautifulSoup(driver.page_source, features='html.parser')


#%%
# Test get_soup_selenium(url)
soup = get_soup_selenium(start_url)
soup

#%%
# Demonstrate occasional anomalies in the ResultSet returned by <BeautifulSoup object>.find_all(<tag>);
# note that they may be appearing only in the selenium version, not in the requests version.

# The following lines find all 'article' tags and show that there are 11 articles on the page, not 10.
# The 11th one is something else, not visible on the page at the first glance and should be eliminated from
# further processing.

articles = soup.find_all('article')
len(articles)

#%%
# The following line shows an anomaly in the articles ResultSet.
articles[10]
# articles[10].a.find_next('a').text
for a in articles:
    print(a['class'])

#%%
# Compare it to any of the other results from the Result set returned by ResultSet
# returned by <BeautifulSoup object>.find_all(<tag>).
articles[0]

#%%
# Demonstrate different ways of getting an attribute value for a tag (a bs4.element.Tag object),
# e.g. <tag>.find('<subtag>'), filtered with <{'class': "<class name>"}>;
# alternatively: <tag>.find('<tag>')['<attr>'], <tag>.find('<subtag>').get('<attribute>'),
# <tag>.find('<subtag>').<attribute>,... (<attribute>: e.g. text)
soup.find('div', {'class': 'article-image-wrapper'})
soup.div['class']
soup.div.attrs
soup.find('div', {'class': 'article-image-wrapper'}).attrs

#%%
# Demonstrate <tag>.find_next_siblings() (returns all <tag>'s siblings) and
# <tag>.find_next_sibling() (returns just the first one);
# e.g., use the 'div' tag, class='rowline clearfix', and find the first 'span' tag in that div (and then its siblings).
div = soup.find('div', {'class': 'rowline clearfix'})
div.span.find_next_sibling()
len(div.span.find_next_siblings())

#%%
# Each bs4.element.ResultSet, bs4.element.Tag,... can be used to create another BeautifulSoup object,
# using BeautifulSoup(str(<bs4.element object>), features='html.parser').

#%%
# Get/Return all text from a bs4.element.Tag object, using <bs4.element.Tag object>.text, e.g. for an 'article' tag.
soup.article.text

#%%
# Get/Return and remove a specific item from a bs4.element.ResultSet using <result set>.pop(<index>) (default: last).
articles = soup.find_all('article')
len(articles)
articles.pop()
len(articles)


#%%
def get_specific_page(start_url: str, page=1) -> str:
    """Returns the URL of a specific page from a Website where long lists of items are split in multiple pages.
    """

    if page > 1:
        return start_url.split('&searchpage=')[0] + '&searchpage=' + str(page)
    return start_url.split('&searchpage=')[0]


#%%
# Test get_specific_page(start_url, page)
get_specific_page(start_url, 2)


#%%
def get_next_soup(start_url: str, page=1):
    """Returns the BeautifulSoup object corresponding to a specific page
    in case there are multiple pages that list objects of interest.
    Parameters:
    - start_url: the starting page/url of a multi-page list of objects
    - page: the page number of a specific page of a multi-page list of objects
    Essentially, get_next_soup() just returns get_soup(get_specific_page(start_url, page)),
    i.e. converts the result of the call to get_specific_page(start_url, page), which is a string,
    into a BeautifulSoup object.
    """

    return get_soup(get_specific_page(start_url, page))


#%%
# Test get_next_soup(start_url: str, page=1)
get_next_soup(start_url, 2).article.text


#%%
def get_next_soup_selenium(start_url: str, page=1):
    """Returns the BeautifulSoup object corresponding to a specific page
    in case there are multiple pages that list objects of interest, using selenium instead of requests.
    Parameters:
    - start_url: the starting page/url of a multi-page list of objects
    - page: the page number of a specific page of a multi-page list of objects
    Essentially, get_next_soup() just returns get_soup_selenium(get_specific_page(start_url, page)),
    i.e. converts the result of the call to get_specific_page(start_url, page), which is a string,
    into a BeautifulSoup object.
    """

    return get_soup_selenium(get_specific_page(start_url, page))


#%%
# Test get_next_soup_selenium(start_url: str, page=1)
get_next_soup_selenium(start_url, 2).article.text


#%%
def crawl(url: str, max_pages=1):
    """Web crawler that collects info about specific articles from Ultimate Classic Rock,
    implemented as a Python generator that yields BeautifulSoup objects (get_next_soup() or get_next_soup_selenium())
    from multi-page article lists.
    Parameters: the url of the starting page and the max number of pages to crawl in case of multipage lists.
    """

    for page in range(1, max_pages+1):
        yield get_next_soup_selenium(url, page)


#%%
# Test crawl(url: str, max_pages=1)
g = crawl(start_url, 3)
while 123:
    try:
        next_soup = next(g)
        print(next_soup.article.text)
    except:
        break


#%%
def get_article_info(article: Tag):
    """
    Returns structured information about an article related to The Beatles,
    extracted from a multi-page article list.
    :param article: a bs4.element.Tag representing the entire article
    :return: a 4-tuple of info-items about the article, including:
    - article_title - the title of the article
    - article_author - the author of the article
    - article_date - the date when the article has been published
    - featured_image_url - the URL of the featured image of the article
    """

    figure = article.figure
    content = article.find('div', {'class': 'content'})

    article_title = content.a.text
    article_author = content.em.text.split('by')[1].strip()
    article_date = content.time.text
    featured_image_url = figure.img['src']

    return article_title, article_author, article_date, featured_image_url


#%%
def get_article_info_list(start_url: str, max_pages=1):
    """
    Returns structured information about articles related to The Beatles from a multi-page article list.
    :param start_url: the url of the starting page of a multi-page article list
    :param max_pages: the max number of pages to crawl
    :return: a list of 4-tuples of info-items about the articles from a multi-page article list
    Calls get_article_info() in a loop to collect the list of tuples, each tuple containing the following data:
    - article_title - the title of an article
    - article_author - the author of an article
    - article_date - the date when an article has been published
    - featured_image_url - the URL of the featured image of an article
    The other relevant data items:
    - article_info_list - the list of article_info 4-tuples for all articles on the site
    """

    article_info_list = []
    g = crawl(start_url, max_pages)

    while 1:
        try:
            s = next(g)
            articles = s.find_all('article')[:-1]
            for a in articles:
                article_info_list.append(get_article_info(a))
        except:
            break

    return article_info_list


#%%
a = soup.article
a.img['src']
a.find('div', {'class': 'content'}).a.text
a.find('div', {'class': 'content'}).em.text.split('by')[-1].strip()
a.find('div', {'class': 'content'}).time.text

#%%
# Test get_article_info_list(start_url: str, max_pages=1)

article_info_list = get_article_info_list(start_url, 3)

#%%
article_info_list

#%%
# Put everything in a csv file

import pandas as pd
# Create a dataframe of articles as <pd.df> = pd.DataFrame(<list>, columns=['<Column 1>', '<Column 2>', ...])
articles_df = pd.DataFrame(article_info_list, columns=['Title', 'Author', 'Date', 'ImageURL'])
# Save the dataframe as a .csv file using <pd.df>.to_csv('../data/...', index=False)
articles_df.to_csv('../data/articles.csv', index=False)

#%%
pd.read_csv('../data/articles.csv')
