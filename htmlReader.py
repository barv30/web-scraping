import requests
from bs4 import BeautifulSoup


# this class gets html page by get request and parses html page, by using BeautifulSoup
class HtmlReader:

    @staticmethod
    def send_get_request_to_url(url):
        page = requests.get(url)
        return page

    @staticmethod
    def parse_html(url):
        page = HtmlReader.send_get_request_to_url(url)
        soup = ""
        if page.status_code == 200:
            soup = HtmlReader.parse_page(page.content)
        return soup

    @staticmethod
    def parse_page(html_byte_arr):
        soup = BeautifulSoup(html_byte_arr, 'html.parser')
        return soup
