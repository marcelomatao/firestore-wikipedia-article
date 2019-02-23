import application.model.wiki_article
from application.db import wiki_dao
from application.wiki.wiki_load import WikiFile2Firestore
from application.wiki.wiki_read import WikiReader

class App:

    def __init__(self, file):
        self.file = file
        self.wikiFileLoader = WikiFile2Firestore(wiki_dao)
        self.wikiFileReader = WikiReader(wiki_dao)
    
    def run(self):
        self.wikiFileLoader.random_load(self.file, 1)

    def run_read(self):
        self.wikiFileReader.read_all_articles()