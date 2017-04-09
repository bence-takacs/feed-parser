from fp import FeedParser


def test_result():
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

