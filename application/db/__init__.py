from application.db.firebase_manager import FirestoreManager
from application.db.wiki_db import WikiDao

farestoreManager = FirestoreManager()
wiki_dao = WikiDao(farestoreManager)