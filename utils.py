import os
import re
import markdown
import yaml

def list_markdown_files(folder_path='./notes'):
    """
    Recursively scan the given folder and return a list of Markdown (.md) file paths.
    """
    markdown_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def parse_markdown_file(file_path):
    """
    Read a Markdown file and extract optional YAML front matter along with the content.

    Args:
        file_path (str): Path to the Markdown file.

    Returns:
        tuple: (metadata, content)
            - metadata (dict or None): Parsed YAML metadata if available, else None.
            - content (str): Markdown content (without the YAML front matter).
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    meta_data = None
    # Check if file starts with YAML front matter (---)
    if content.startswith('---'):
        # Split the content on the first two occurrences of '---'
        parts = content.split('---', 2)
        if len(parts) >= 3:
            raw_meta = parts[1]
            content = parts[2]
            if yaml:
                try:
                    meta_data = yaml.safe_load(raw_meta)
                except Exception as e:
                    print(f"Warning: Failed to parse YAML metadata in {file_path}: {e}")
                    meta_data = None
            else:
                print("Warning: PyYAML is not installed. Skipping YAML metadata parsing.")

    return meta_data, content

def markdown_to_plain_text(markdown_text):
    """
    Convert Markdown text to plain text.
    
    This function first converts Markdown to HTML using the 'markdown' package,
    then removes HTML tags to produce plain text.
    
    Args:
        markdown_text (str): Raw Markdown content.
        
    Returns:
        str: Plain text extracted from the Markdown.
    """
    # Convert Markdown to HTML
    html = markdown.markdown(markdown_text)
    # Use a simple regex to remove HTML tags
    plain_text = re.sub('<[^<]+?>', '', html)
    return plain_text