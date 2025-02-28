# Technical Notes

### Indexing `indexer.py`

- Reads all .md files from the target folder.
- Extracts content and optional YAML metadata.
- Converts text into embeddings using SentenceTransformers.
- Stores embeddings in a FAISS index (faiss_index.index).
- Saves metadata mappings (metadata_mapping.json).

### Searching `searcher.py`

- Loads the FAISS index and metadata.
- Embeds the search query.
- Performs nearest-neighbor search using FAISS.
- Returns the top K most similar notes.


## 📚 Dependencies

Package	Purpose

- `faiss-cpu`	Efficient vector search engine
- `sentence-transformers`	Generates embeddings from markdown text
- `typer`	Elegant command-line interface
- `rich` Beautiful CLI output
- `pyyaml`	Parses YAML metadata from markdown notes

```mermaid
graph TD
	subgraph Indexing
	    A[Start Indexing] --> B[Read Markdown Files] --> C[Extract Content & Metadata]
	    C --> D[Convert Text to Embeddings SentenceTransformers]
	    D --> E[Store Embeddings in FAISS Index faiss_index.index]
	    D --> F[Save Metadata Mappings metadata_mapping.json]
	end
	
	subgraph Searching
		G[Start Searching] --> H[Load FAISS Index & Metadata]
		H --> I[Embed Search Query SentenceTransformers]
		I --> J[Perform Nearest-Neighbor Search with FAISS]
		J --> K[Return Top K Most Similar Notes]
		E --> H
		F --> H
	end
```
