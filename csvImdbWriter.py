from csv import writer
from imdbHtmlReader import ImdbHtmlReader


# this class gets html data by calling methods from ImdbHtmlReader class, opens new csv file and writes the data to the
# file
class CsvImdbWriter:

    @staticmethod
    def write_csv_imdb_file(movies):
        with open('imdb_movies.csv', 'w', encoding='utf8', newline='') as f:
            thewriter = writer(f)
            CsvImdbWriter.get_data_and_write(movies, thewriter)

    @staticmethod
    def get_data_and_write(movies, thewriter):
        header = ['Rank', 'Title', 'Year', 'Rating', 'URL']
        thewriter.writerow(header)
        for movie in movies:
            title = ImdbHtmlReader.get_movie_title(movie)
            rank = ImdbHtmlReader.get_movie_rank(movie)
            year = ImdbHtmlReader.get_movie_year(movie)
            rating = ImdbHtmlReader.get_movie_rating(movie)
            url = ImdbHtmlReader.get_movie_link(movie)
            row = [rank, title, year, rating, url]
            thewriter.writerow(row)
