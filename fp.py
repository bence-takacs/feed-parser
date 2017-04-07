#!/usr/bin/env python

import sys
import requests
import json
from bs4 import BeautifulSoup
import logging


def get_text(str):
    if str.startswith("http://") or str.startswith("https://"):
        return get_text_from_url(str)
    else:
        return get_text_from_file(str)


def get_text_from_url(url):
    if url is None:
        log.error("URL should not be null")
    else:
        log.info("--SITE: " + url)
        source_code = requests.get(url)
        return source_code.content


def get_text_from_file(file_path):
    if file_path is None:
        log.error("FILE PATH should not be null")
    else:
        log.info("--FILE PATH: " + file_path)
        try:
            return open(file_path, 'r')
        except Exception as e:
            log.error('Failed to open file: ' + file_path, exc_info=True)


def get_feed_links(source_path, source_text, out_file_path):
    if source_text is None:
        log.error("URL should not be null")
    else:
        soup = BeautifulSoup(source_text, "html.parser")
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


logging.basicConfig(format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s", filename='fp.log', level=logging.DEBUG)
log = logging.getLogger(__name__)

output = sys.argv[2] if len(sys.argv) > 2 else "./output.json"
input = sys.argv[1] if len(sys.argv) > 1 else "./input.html"

get_feed_links(input, get_text(input), output)

