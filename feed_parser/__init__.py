from FeedParser import FeedParser
import sys

def cmd_line():
    output = sys.argv[2] if len(sys.argv) > 2 else None
    input = sys.argv[1] if len(sys.argv) > 1 else None

    fp = FeedParser(input, output)
    fp.parse()


