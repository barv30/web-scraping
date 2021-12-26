from urllib.parse import urljoin


# this class reads html data from IMDB html
class ImdbHtmlReader:

    def __init__(self, html_page):
        self.htmlPage = html_page

    def get_html_page(self):
        return self.htmlPage

    def get_movies_list(self, elementName, className):
        movies = self.htmlPage.find(elementName, class_=className).find_all('tr')
        return movies

    @staticmethod
    def get_movie_title(movie):
        title = movie.find('td', class_='titleColumn').a.text
        return title

    @staticmethod
    def get_movie_rank(movie):
        rank = movie.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]
        return rank

    @staticmethod
    def get_movie_rating(movie):
        rating = movie.find('td', class_='ratingColumn imdbRating').strong.text
        return rating

    @staticmethod
    def get_movie_year(movie):
        year = movie.find('td', class_='titleColumn').span.text.strip('()')
        return year

    @staticmethod
    def get_movie_link(movie):
        base = "https://www.imdb.com"
        a_href = movie.find('td', class_='titleColumn').a['href']
        link = urljoin(base, a_href)
        return link
