import typer
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
import indexer
import searcher

app = typer.Typer()
console = Console()

@app.command()
def index(
    folder: str = typer.Option(..., help="Path to the Markdown notes folder")
):
    """
    Build the FAISS index from Markdown notes in the specified folder.
    """
    console.print("[bold green]Starting the indexing process...[/bold green]")
    indexer.build_index(notes_folder=folder)
    console.print("[bold green]Indexing complete.[/bold green]")

@app.command()
def search(
    query: str = typer.Option(..., help="Search query"),
    k: int = typer.Option(5, help="Number of search results to return")
):
    """
    Perform a one-shot search on the FAISS index using the provided query.
    """
    console.print(f"[bold blue]Searching for:[/bold blue] {query}")
    results = searcher.search(query, k)
    
    if results:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("File Path", style="dim", width=40)
        table.add_column("Score", justify="right")
        table.add_column("Metadata", style="dim", width=30)
        for res in results:
            file_path = res.get("file_path", "N/A")
            score = f"{res.get('score', 0):.2f}"
            metadata = str(res.get("metadata", ""))
            table.add_row(file_path, score, metadata)
        console.print(table)
    else:
        console.print("[bold red]No results found.[/bold red]")

@app.command()
def interactive(
    k: int = typer.Option(5, help="Number of search results to return for each query")
):
    """
    Launch an interactive search session. Type your query, see the results, and repeat.
    Type 'exit' or 'quit' to end the session.
    """
    console.print(Panel("[bold green]Interactive Search Mode[/bold green]", expand=True))
    while True:
        # Use console.input to render the prompt with Rich markup
        query = console.input("[bold blue]>> [/bold blue]")
        if query.strip().lower() in ("exit", "quit"):
            console.print("[bold red]Exiting interactive search mode.[/bold red]")
            break
        
        results = searcher.search(query, k)
        if results:
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("File Path", style="dim", width=40)
            table.add_column("Score", justify="right")
            # table.add_column("Metadata", style="dim", width=30)
            for res in results:
                file_path = res.get("file_path", "N/A")
                score = f"{res.get('score', 0):.2f}"
                #metadata = str(res.get("metadata", ""))
                table.add_row(file_path, score)
            console.print(table)
        else:
            console.print("[bold red]No results found.[/bold red]")

if __name__ == "__main__":
    app()
