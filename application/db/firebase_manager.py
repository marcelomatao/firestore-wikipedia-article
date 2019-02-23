import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

class FirestoreManager:
    
    def __init__(self):
        credentials_path = os.environ['GCP_FIREBASE_TEXT_CLASSIFICATION']
        cred = credentials.Certificate(credentials_path)
        self.app = firebase_admin.initialize_app(cred)
        self.client = firestore.client(app=self.app)