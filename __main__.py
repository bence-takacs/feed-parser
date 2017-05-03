import feed_parser.FeedParser
import web


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



