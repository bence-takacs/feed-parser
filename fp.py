#!/usr/bin/env python
#pip install -r requirements.txt

import requests
from bs4 import BeautifulSoup
import logging
#from logging.config import fileConfig
import json


def get_feed_links_from_url(url, out_file_path):
    if url is None:
        log.error("URL should not be null")
    else:
        log.info("--SITE: " + url)
        source_code = requests.get(url)
        plain_text = source_code.text
        get_feed_links(url, plain_text, out_file_path)


def get_feed_links_from_file(file_path, out_file_path):
    if file_path is None:
        log.error("FILE PATH should not be null")
    else:
        log.info("--FILE PATH: " + file_path)
        try:
            with open(file_path, 'r') as infile:
                get_feed_links(file_path, infile, out_file_path)
        except Exception as e:
            log.error('Failed to open file: ' + file_path, exc_info=True)


def get_feed_links(source_path, source_text, out_file_path):
    if source_text is None:
        log.error("URL should not be null")
    else:
        #BeautifulSoup(open("index.html"))
        soup = BeautifulSoup(source_text, "html.parser")
        #"link", {"type": "application/rss+xml", "type": "application/x.atom+xml"}, "a", {"type" : "application/rss+xml", "type" : "application/x.atom+xml"}
        atom_links = []
        rss_links = []
        for link_rss in soup.find_all(["link", "a"], type="application/rss+xml"):
            rss_links.append(str(link_rss.get('href')))
        for link_atom in soup.find_all(["link", "a"], type="application/x.atom+xml"):
            atom_links.append(str(link_atom.get('href')))
        data = {'rss': rss_links,
                'atom': atom_links}
        log.debug("FEEDS [" + source_path + "] " +json.dumps(data, sort_keys=True, indent = 4))

        with open(out_file_path, 'w') as outfile:
            try:
                json.dump(data, outfile, sort_keys=True, indent = 4)
            except Exception as e:
                log.error('Failed to open file: ' + outfile.name, exc_info=True)


logging.basicConfig(format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s", level=logging.DEBUG)
#logging.basicConfig(filename='fp.log',level=logging.DEBUG)
#fileConfig('logging.ini')
log = logging.getLogger(__name__)

#get_feed_links_from_url("http://index.hu")
get_feed_links_from_file("./input.html", "./output.json")

#get_feed_links("http://origo.hu")

#get_feed_links("http://hvg.hu")

#get_feed_links("http://www.nytimes.com/")

#get_feed_links("http://nationalgeographic.com/")

#get_feed_links("https://thetimes.co.uk/")
