# Semàntica

Similarity search of personal markdown notes.

> "Totally an overkill"

**FAISS** for similarity search, **SentenceTransformers** for embeddings, and **Typer + Rich** for the CLI.

## 🚀 Features

✅ **Similarity search** over a folder of markdown (`.md`) files. Honestly not very fast.
✅ **Supports YAML metadata** extraction for richer context in search results. Because I take my notes in [Obsidian.md](htps://obsidian.md).
✅ **Beautifil CLI**.  
✅ **Choose you embedding** (default: `all-MiniLM-L6-v2`).  

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

> [!WARNING] Tested only with `faiss-cpu`, as present in the requirements, if you want to try with faiss-gpu have to install it from source.


## Usage

### Build the Index

Before searching, you need to index your markdown files. This processes all .md files in the ./notes folder and builds a FAISS index.

```bash
cd src
python cli.py index --folder ../notes
```

### Interactive Search

![Search Demo](demo.gif)

Launch an interactive search session. Sets `--k` to the number of item shown per search.

```bash
python cli.py interactive --k 10
``` 

## Configuration & Customization

### Configuration

Change the `config.py` file in `/src`.

### Embeddings Model

By default, the project uses all-MiniLM-L6-v2 from sentence-transformers. To change the model, modify `config.py`:

```python
EMBEDDING_MODEL = "sentence-transformers/all-mpnet-base-v2"
```

Other great models:

- all-MiniLM-L6-v2 (fast & lightweight, default)
- all-mpnet-base-v2 (higher accuracy)
- multi-qa-MiniLM-L6-dot-v1 (optimized for QA)
- nomic-ai/nomic-embed-text-v1 (great for large datasets)

More models here: [Hugging Face Model Hub](https://huggingface.co/docs/hub/models-the-hub)

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

# ⚖️ License

This project is licensed under the MIT License.
See the full license in LICENSE.

# Star This Project!

If you find this project useful, please consider starring ⭐ it on GitHub!