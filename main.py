import typer

app = typer.Typer()

@app.command()
def hello(name: str, formal: bool = False):
    """
    Greet a user by their NAME.
    """
    if formal:
        typer.echo(f"Good day, Distinguished Guest {name}.")
    else:
        typer.echo(f"Hello, {name}! Welcome to reporadar! Run info for all commands!")

@app.command()
def info():
    """
    Get latest information about reposcan
    """
    typer.echo("Hello User! I built reposcan so you can easily manage all your repositories easily from your terminal. reposcan is completely free and \n open-source!")

@app.command()
def scan(folder: str):
    """
    Scans your selected folder and presents all your repositories.
    """
    typer.echo(f"Below, are your git repositories in your selected folder \n {folder}")
