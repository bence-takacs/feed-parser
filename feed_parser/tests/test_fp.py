from feed_parser import FeedParser


def test_end_to_end():
    #GIVEN
    undertest = FeedParser("http://origo.hu")

    #WHEN
    rss_links = undertest.parse()
    print type(rss_links)
    print rss_links

    #THEN
    assert(rss_links)
    assert(len(rss_links) > 0)
    assert(rss_links[0]=='http://www.origo.hu/contentpartner/rss/origoall/origo.xml')

def unit_test():
    # GIVEN
    undertest = FeedParser("")

    # WHEN
    rss_links = undertest.parse()
    print type(rss_links)
    print rss_links

    # THEN
    assert (rss_links)
    assert (len(rss_links) > 0)
    assert (rss_links[0] == 'http://www.origo.hu/contentpartner/rss/origoall/origo.xml')
