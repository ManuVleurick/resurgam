import requests
from bs4 import BeautifulSoup
from book_database_app.config.glob_vars import URL_GENTBIB,AANTAL_RESULTS
from book_database_app.config.loggers import logger_repo

class BooksRepository:

    def _get_soup(self,url):
        req = requests.get(url)
        soup = BeautifulSoup(req.content,'html.parser')
        return soup

    #Eerste gegeven resultaten van gent_bib
    def get_results_bib_from_book(self,query):
        logger_repo.info('Start scraping gent bib site')
        url = URL_GENTBIB+query
        soup = self._get_soup(url)
        formats = [item.get_text() for item in soup.find_all('div',{"class":"main-format"})]
        titles = [title.get_text().replace('\n','').replace(' ','') for title in soup.find_all("h3",{"class":"catalog-item-title"})]
        del titles[1::2]
        links = [item.get('href') for item in soup.find_all('a',class_='catalog-item-title-link')]
        del links[1::2]
        links = ['https://gent.bibliotheek.be'+item for item in links]
        imgs = [item.get("src") for item in soup.find("div",{"class":"search-results"}).find_all("img")]
        authors = [item.find_next('a').get_text().replace(' ','').replace('\n','') for item in soup.find_all('div',{"class":"catalog-item__authors"})]
        del authors[1::2]
        languages = [item.get_text() for item in soup.find_all('div',{"class":"catalog-item__type--language"})]
        bib_plaatsen = []
        descriptions = []
        ISBNs = []
        formats = formats[:AANTAL_RESULTS]
        titles = titles[:AANTAL_RESULTS]
        links = links[:AANTAL_RESULTS]
        imgs = imgs[:AANTAL_RESULTS]
        authors = authors[:AANTAL_RESULTS]
        languages = languages[:AANTAL_RESULTS]

        for img in imgs:
            self._download_img(img)

        logger_repo.info('Scraping gent bib done!')
        data = {'formats':formats,'titles':titles,'links':links,'authors':authors,'languages':languages}
        return data

    #Downloads image to resources/img and name is book_id
    def _download_img(self,img_url):
        pass

    #returnt (review,review_score)
    def find_review(self,book_id):
        pass

