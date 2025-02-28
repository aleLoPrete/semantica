# 📝 Semàntica

Semantic earch(FAISS) of markdown notes.

A fast, efficient, and visually appealing **command-line search tool** for markdown notes.  
This CLI leverages **FAISS** for similarity search, **SentenceTransformers** for embeddings, and **Typer + Rich** for an interactive, user-friendly interface.

## 🚀 Features

✅ **Fast semantic search** over a folder of markdown (`.md`) files.  
✅ **Supports YAML metadata** extraction for richer context in search results.  
✅ **Interactive search mode** with a beautiful CLI interface using `Typer` & `Rich`.  
✅ **Customizable embeddings model** (default: `all-MiniLM-L6-v2`).  
✅ **Optimized FAISS indexing** for efficient nearest-neighbor retrieval.  


## 📌 Installation

Ensure you have Python **3.8+** installed.

### Clone the repository

```bash
git clone https://github.com/aleloprete/semantica.git
cd markdown-search-cli
```

### Install dependencies

```bash
pip install -r requirements.txt
```

> [!warning] I tested only faiss-cpu, as present in the requirements, if you want to try with faiss-gpu have to install it from source.


## 🏗️ Usage

### Build the Index

Before searching, you need to index your markdown files. This processes all .md files in the ./notes folder and builds a FAISS index.

```bash
python cli.py index --folder ./notes
```


### One shot Search

Search directly from the CLI with a one-shot query:

```bash
python cli.py search --query "encryption algorithms" --k 5
```

Example Output:

```bash
Searching for: encryption algorithms
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ File Path                                ┃ Score ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ notes/crypto.md                          │ 0.87  │
│ notes/encryption.md                      │ 0.83  │
│ notes/secure-comms.md                    │ 0.79  │
└──────────────────────────────────────────┴───────┘
```

### Interactive Search

Launch an interactive search session:

```bash
python cli.py interactive
``` 
This lets you continuously enter search terms and see results dynamically. Type exit or quit to exit.

## 🔧 Configuration & Customization

### ✅ Change the Embeddings Model
By default, the project uses all-MiniLM-L6-v2 from sentence-transformers.
To change the model, modify searcher.py:

```python
MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"  # Example: more powerful model
```

Other great models:

- all-MiniLM-L6-v2 (fast & lightweight, default)
- all-mpnet-base-v2 (higher accuracy)
- multi-qa-MiniLM-L6-dot-v1 (optimized for QA)
- nomic-ai/nomic-embed-text-v1 (great for large datasets)

Find more models here: Hugging Face Model Hub

## 🏗️ How It Works (Technical Overview)

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


### 📚 Dependencies

Package	Purpose

- `faiss-cpu`	Efficient vector search engine
- `sentence-transformers`	Generates embeddings from markdown text
- `typer`	Elegant command-line interface
- `rich` Beautiful CLI output
- `pyyaml`	Parses YAML metadata from markdown notes

## 🛠️ Troubleshooting

- Make sure FAISS is installed correctly:

```bash
pip install faiss-cpu
```

- Ensure the index command has been run before searching.

```bash
python cli.py index --folder ./notes
```

- Missing dependencies?

```bash
pip install -r requirements.txt
```

## 👥 Contributing

🚀 PRs are welcome! If you have ideas for:

- More efficient indexing/searching
- Improved metadata handling
- GUI enhancements
- Feel free to open an issue or submit a pull request.

# ⚖️ License
This project is licensed under the MIT License.
See the full license in LICENSE.

# ⭐ Star This Project!
If you find this project useful, please consider starring ⭐ it on GitHub!