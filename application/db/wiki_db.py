from application.db.firebase_manager import FirestoreManager
import json
import uuid

class WikiDao:

    def __init__(self, firestore_manager):
        self.firestore_manager = firestore_manager
        self.db = firestore_manager.client

    def set_wiki_article(self, wiki_article):
        #print(wiki_article.uuid)
        # print(json.dumps(wiki_article.__dict__))
        doc_ref = self.db.collection(u'article').document(wiki_article.uuid)
        doc_ref.set(wiki_article.__dict__)

    def read_wiki_articles(self):
        article_ref = self.db.collection(u'article')
        docs = article_ref.get()

        for doc in docs:
            print(u'{} => {}'.format(doc.id, doc.to_dict()))
