import xml.etree.ElementTree as etree
from application.model.wiki_article import WikiArticle
import random

class WikiFile2Firestore:

    def __init__(self, wiki_dao):
        self.wiki_dao = wiki_dao

    def readWikiArticle(self, pre_tag, elem):
        title = ""
        page_id = -1
        revision_id = -1 
        parent_id = -1 
        timestamp = ""
        text = ""
        for child in elem:
            if child.tag == pre_tag+'title':
                title = child.text
            if child.tag == pre_tag+'id':
                page_id = child.text
            if child.tag == pre_tag+'revision':
                for c in child:
                    if c.tag == pre_tag+'id':
                        revision_id = c.text
                    if c.tag == pre_tag+'parentid':
                        parent_id = c.text
                    if c.tag == pre_tag+'timestamp':
                        timestamp = c.text
                    if c.tag == pre_tag+'text':
                        text = c.text
        return WikiArticle(title, page_id, revision_id, parent_id, timestamp, text)


    def random_load(self, file, number_of_articles):
        n = 0
        pre_tag = '{http://www.mediawiki.org/xml/export-0.10/}'

        step = 100
        takeElem = random.randint(1, step)
        i = 0
        for event, elem in etree.iterparse(file, events=('start', 'end')):
            
            if event == 'end':
                if elem.tag == pre_tag+'page':
                    if i == takeElem:
                        wiki = self.readWikiArticle(pre_tag, elem)
                        
                        if "#REDIRECT" not in wiki.text: 
                            n = n + 1
                            print('sending article')
                            self.wiki_dao.set_wiki_article(wiki)
                        else:
                            print('redirect article')
                        takeElem = takeElem + random.randint(1, step)
                    i = i + 1
                if n == number_of_articles:
                    break