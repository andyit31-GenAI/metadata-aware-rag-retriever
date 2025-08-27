from langchain.vectorstores import Chroma
from langchain.schema import Document

class MetadataAwareRetriever:
    def __init__(self, persist_directory="db"):
        self.db = Chroma(persist_directory=persist_directory)

    def get_documents(self, query, filters=None):
        if filters:
            return self.db.similarity_search(query, filter=filters, k=5)
        else:
            return self.db.similarity_search(query, k=5)
