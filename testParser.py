import unittest

from htmlReader import HtmlReader
from imdbHtmlReader import ImdbHtmlReader
from main import App
import os.path


class TestParse(unittest.TestCase):

    def test_url_parse(self):
        htmlParse = HtmlReader.parse_html("https://www.udemy.com/")
        self.assertNotEqual(htmlParse, "", "Error in URL parsing")

    def test_parser(self):
        htmlParse = HtmlReader.parse_html("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
        imdbHtmlReader = ImdbHtmlReader(htmlParse)
        movies = imdbHtmlReader.get_movies_list('tbody', "lister-list")
        self.assertNotEqual(movies, "", "Error in URL parsing")

    def test_file_created(self):
        a = App()
        a.execute("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
        self.assertTrue(os.path.isfile("imdb_movies.csv"))


if __name__ == '__main__':
    unittest.main()
