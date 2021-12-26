from htmlReader import HtmlReader
from imdbHtmlReader import ImdbHtmlReader
from csvImdbWriter import CsvImdbWriter
import os.path


# the class gets IMDB website url, gets html of IMDB page and writes top 250 movies details to csv file
class App:
    pass

    def execute(self, url):
        if os.path.isfile("imdb_movies.csv"):
            os.remove("imdb_movies.csv")
        htmlParse = HtmlReader.parse_html(url)
        if htmlParse:  # if html page is not empty - continue the process
            imdbHtmlReader = ImdbHtmlReader(htmlParse)
            movies = imdbHtmlReader.get_movies_list('tbody', "lister-list")
            CsvImdbWriter.write_csv_imdb_file(movies)
        else:
            print('There is a problem to parse the url')


app = App()
app.execute("https://www.imdb.com/chart/top/?ref_=nv_mv_250")

