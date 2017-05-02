from FeedParser import FeedParser
import sys
import web

def cmd_line():
    output = sys.argv[2] if len(sys.argv) > 2 else None
    input = sys.argv[1] if len(sys.argv) > 1 else None

    fp = FeedParser(input, output)
    fp.parse()

def main():
    urls = (
        '/', 'FeedParser',
        '/feeds/(.*)', 'FeedParser'
    )

    app = web.application(urls, globals())
    web.httpserver.runsimple(app.wsgifunc(), ("0.0.0.0", 8080))
    app.run()

if __name__ == "__main__":
    main()
