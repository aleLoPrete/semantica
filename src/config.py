import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOTES_FOLDER = os.path.abspath(os.path.join(BASE_DIR, "../notes"))
DATA_FOLDER = os.path.abspath(os.path.join(BASE_DIR, "../data"))

FAISS_INDEX_PATH = os.path.join(DATA_FOLDER, "faiss_index.index")
METADATA_PATH = os.path.join(DATA_FOLDER, "metadata_mapping.json")

# Embedding Model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"