from application.model.wiki_article import WikiArticle
import random

class WikiReader:

    def __init__(self, wiki_dao):
        self.wiki_dao = wiki_dao

    def read_all_articles(self):
        self.wiki_dao.read_wiki_articles()