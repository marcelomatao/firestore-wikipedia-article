import uuid

class WikiArticle:
    
    def __init__(self, title, page_id, revision_id, parent_id, timestamp, text):
        self.uuid = str(uuid.uuid4())
        self.title = title
        self.page_id = page_id
        self.revision_id = revision_id
        self.parent_id = parent_id
        self.timestamp = timestamp
        self.text = text

    def __repr__(self):
        return '<WikiArticle %r>' % str(self.uuid)
