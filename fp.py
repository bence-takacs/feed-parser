#!/usr/bin/env python
#pip install -r requirements.txt

import requests
from bs4 import BeautifulSoup
import json

def get_feed_links(website_url):
    if website_url is None:
        print("URL should not be null")
    else:
        source_code = requests.get(website_url)
        plain_text = source_code.text
        #BeautifulSoup(open("index.html"))
        soup = BeautifulSoup(plain_text, "html.parser")
        #"link", {"type": "application/rss+xml", "type": "application/x.atom+xml"}, "a", {"type" : "application/rss+xml", "type" : "application/x.atom+xml"}
        atom_links = []
        rss_links = []
        for link in soup.find_all("link", {"type" : "application/rss+xml"}):
            link = str(link.get('href'))
            rss_links.append(link)
        for link in soup.find_all("link", {"type" : "application/x.atom+xml"}):
            link = str(link.get('href'))
            atom_links.append(link)
        for link in soup.find_all("a", {"type" : "application/rss+xml"}):
            link = str(link.get('href'))
            rss_links.append(link)
        for link in soup.find_all("a", {"type" : "application/x.atom+xml"}):
            link = str(link.get('href'))
            atom_links.append(link)
        print json.dumps({'rss': rss_links, 'atom': atom_links}, sort_keys=True, indent = 4)

        #with open('data.txt', 'w') as outfile:
        #json.dump(data, outfile)

get_feed_links("http://index.hu")

get_feed_links("http://origo.hu")

get_feed_links("http://hvg.hu")

get_feed_links("http://www.nytimes.com/")

get_feed_links("http://nationalgeographic.com/")

get_feed_links("https://thetimes.co.uk/")

