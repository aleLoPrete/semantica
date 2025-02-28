import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from config import FAISS_INDEX_PATH, METADATA_PATH, EMBEDDING_MODEL

#INDEX_PATH = 'faiss_index.index'
#MAPPING_PATH = 'metadata_mapping.json'
#MODEL_NAME = 'all-MiniLM-L6-v2'

def search(query, k=5):
    """
    Search the FAISS index for the given query and return results.

    Args:
        query (str): The text query.
        k (int): Number of nearest neighbors to retrieve.

    Returns:
        list of dict: Each dict contains 'file_path', 'metadata', and 'score'.
    """
    # Load the FAISS index from disk.
    index = faiss.read_index(FAISS_INDEX_PATH)

    # Load the metadata mapping (keys are stored as strings in JSON).
    with open(METADATA_PATH, 'r', encoding='utf-8') as f:
        mapping = json.load(f)

    # Load the embedding model.
    model = SentenceTransformer(EMBEDDING_MODEL)

    # Compute the embedding for the query.
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype('float32')

    # Perform the search in the FAISS index.
    scores, indices = index.search(query_embedding, k)

    results = []
    for i, idx in enumerate(indices[0]):
        if idx == -1:
            continue
        # Since JSON converts dict keys to strings, check using str(idx).
        file_info = mapping.get(str(idx)) or mapping.get(idx)
        if not file_info:
            continue
        results.append({
            "file_path": file_info.get("file_path"),
            "metadata": file_info.get("metadata"),
            "score": float(scores[0][i])
        })
    return results

# For quick testing from the command line.
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        results = search(query)
        for res in results:
            print(f"File: {res['file_path']}\nScore: {res['score']}\nMetadata: {res['metadata']}\n")
    else:
        print("Please provide a search query.")
