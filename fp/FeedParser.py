#!/usr/bin/env python

import requests
import json
from bs4 import BeautifulSoup
import logging
import sys


class FeedParser:
    """A feed parser that needs an input html file.
    """

    def __init__(self, input="./input.html", output="./output.json"):
        """Return a FeedParser object which can parse the *input* and put the 
        result into *output*."""
        self.input = input
        self.output = output
        logging.basicConfig(format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s", filename='fp.log',
                            level=logging.DEBUG)
        self.log = logging.getLogger(__name__)

    def extract_text_from_path(self):
        if self.input.startswith("http://") or self.input.startswith("https://"):
            return self.get_text_from_url(self.input)
        else:
            return self.get_text_from_file(self.input)

    def get_text_from_url(self, url):
        if url is None:
            self.log.error("URL should not be null")
        else:
            self.log.info("--SITE: " + url)
            source_code = requests.get(url)
            return source_code.content

    def get_text_from_file(self, file_path):
        if file_path is None:
            self.log.error("FILE PATH should not be null")
        else:
            self.log.info("--FILE PATH: " + file_path)
            try:
                return open(file_path, 'r')
            except Exception as e:
                self.log.error('Failed to open file: ' + file_path, exc_info=True)

    def parse(self):
        """Parses the *input* and put the 
        result into *output*."""
        source_text=fp.extract_text_from_path()
        if source_text is None:
            self.log.error("URL should not be null")
        else:
            soup = BeautifulSoup(source_text, "html.parser")
            rss_links = []
            atom_links = []
            for link_rss in soup.find_all(["link", "a"], type="application/rss+xml"):
                rss_links.append(str(link_rss.get('href')))
            for link_atom in soup.find_all(["link", "a"], type="application/x.atom+xml"):
                atom_links.append(str(link_atom.get('href')))
            data = {'rss': rss_links,
                    'atom': atom_links}
            self.log.debug("FEEDS [" + self.input + "] " +json.dumps(data, sort_keys=True, indent = 4))

            with open(self.output, 'w') as outfile:
                try:
                    json.dump(data, outfile, sort_keys=True, indent = 4)
                except Exception as e:
                    self.log.error('Failed to open file: ' + outfile.name, exc_info=True)
            return rss_links, atom_links


output = sys.argv[2] if len(sys.argv) > 2 else None
input = sys.argv[1] if len(sys.argv) > 1 else None

fp = FeedParser(input, output)
fp.parse