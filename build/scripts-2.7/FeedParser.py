#!/usr/bin/python

import requests
import json
from bs4 import BeautifulSoup
import logging


class FeedParser:
    """A feed parser that needs an input html file.
    """

    def __init__(self, infile=None, outfile=None):
        """Return a FeedParser object which can parse the *input* and put the 
        result into *output*."""
        self.infile = infile or "./input.html"
        self.outfile = outfile or "./output.json"
        logging.basicConfig(format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s", filename='fp.log',
                            level=logging.DEBUG)
        self.log = logging.getLogger(__name__)

    def GET(self):
        return "No site defined. Please use /feeds/(.*) to define the site. E.g: /feeds/index.hu"

    def GET(self, site_link):
        site_link = site_link if site_link.startswith("http") else "http://"+site_link
        fp = FeedParser(site_link)
        self.log.debug("SITE [" + site_link + "] ")
        return fp.parse()

    def extract_text_from_path(self):
        if self.infile.startswith("http://") or self.infile.startswith("https://"):
            return self.get_text_from_url(self.infile)
        else:
            return self.get_text_from_file(self.infile)

    def get_text_from_url(self, url):
        if url is None:
            self.log.error("URL should not be null")
        else:
            self.log.info("--URL: " + url)
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
        source_text=self.extract_text_from_path()
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
            out = json.dumps(data, sort_keys=True, indent = 4)
            self.log.debug("FEEDS [" + self.infile + "] " + out)
            return out

