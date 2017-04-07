#!/usr/bin/env python
#pip install -r requirements.txt

import requests
from bs4 import BeautifulSoup
import logging
#from logging.config import fileConfig
import json


def get_feed_links(website_url):
    if website_url is None:
        print("URL should not be null")
    else:
        log.info("--SITE: "+website_url)
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
        data = {'rss': rss_links,
                'atom': atom_links}
        log.debug("FEEDS [http://index.hu" + "] " +json.dumps(data, sort_keys=True, indent = 4))

        with open('./output.json', 'w') as outfile:
            json.dump(data, outfile, sort_keys=True, indent = 4)

logging.basicConfig(level=logging.DEBUG)
#fileConfig('logging.ini')
log = logging.getLogger(__name__)

get_feed_links("http://index.hu")

#get_feed_links("http://origo.hu")

#get_feed_links("http://hvg.hu")

#get_feed_links("http://www.nytimes.com/")

#get_feed_links("http://nationalgeographic.com/")

#get_feed_links("https://thetimes.co.uk/")
