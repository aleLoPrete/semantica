import os
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import utils

def build_index(
    notes_folder='./notes',
    index_path='faiss_index.index',
    mapping_path='metadata_mapping.json',
    model_name='all-MiniLM-L6-v2'
):
    """
    Build a FAISS index from Markdown notes.

    Steps:
      1. List all Markdown files in the folder.
      2. Parse each file to extract YAML metadata and content.
      3. Convert the Markdown content to plain text.
      4. Optionally append the metadata (as JSON) to the plain text.
      5. Compute embeddings for each processed text.
      6. Create a FAISS index (using L2 distance) and add all embeddings.
      7. Save the FAISS index and metadata mapping to disk.

    Args:
        notes_folder (str): Path to the folder containing Markdown notes.
        index_path (str): File path to save the FAISS index.
        mapping_path (str): File path to save the metadata mapping.
        model_name (str): Pre-trained SentenceTransformer model name.
    """
    # List Markdown files
    md_files = utils.list_markdown_files(notes_folder)
    if not md_files:
        print(f"No Markdown files found in {notes_folder}.")
        return

    # Load the embedding model
    print("Loading embedding model...")
    model = SentenceTransformer(model_name)

    texts = []      # Will hold the text content (plus metadata if applicable)
    mapping = {}    # Mapping of index IDs to file paths and metadata

    print("Processing Markdown files...")
    for idx, file_path in enumerate(md_files):
        meta, content = utils.parse_markdown_file(file_path)
        # Convert Markdown to plain text
        plain_text = utils.markdown_to_plain_text(content)
        
        # Option: Include YAML metadata if available
        # Pros: Adds extra context such as tags, dates, and authors.
        # Cons: Might add some noise if metadata is inconsistent.
        # Since metadata is minimal, we append it to the plain text.
        if meta:
            plain_text += "\n" + json.dumps(meta, default=str)
        
        texts.append(plain_text)
        mapping[idx] = {
            "file_path": file_path,
            "metadata": meta
        }

    # Compute embeddings for all texts
    print("Computing embeddings...")
    embeddings = model.encode(texts, show_progress_bar=True)
    embeddings = np.array(embeddings).astype('float32')

    # Create a FAISS index using L2 (Euclidean) distance.
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    print("Adding embeddings to the FAISS index...")
    index.add(embeddings)

    # Save the FAISS index to disk
    faiss.write_index(index, index_path)
    print(f"FAISS index saved to: {index_path}")

    # Save the metadata mapping as JSON
    with open(mapping_path, 'w', encoding='utf-8') as f:
        # default=str converts non-serializable types (like date) to strings.
        json.dump(mapping, f, indent=4, default=str)
    print(f"Metadata mapping saved to: {mapping_path}")

if __name__ == '__main__':
    build_index()
