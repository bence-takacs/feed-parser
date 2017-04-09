from unittest import TestCase

from fp import FeedParser

class FeedParserTest(TestCase):
    def test_result(self):
        #GIVEN
        undertest = FeedParser("http://origo.hu")

        #WHEN
        out = undertest.parse
        #print out

        #THEN
        self.assertTrue(out[0].len > 0)
