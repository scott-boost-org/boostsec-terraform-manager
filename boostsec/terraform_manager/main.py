"""Entrypoint."""
import typer

app = typer.Typer()


@app.command()
def version() -> None:
    """Version."""
    typer.echo("Version 0.0.1")


@app.command()
def create() -> None:
    """Create."""
    typer.echo("Create an org")


@app.command()
def delete() -> None:
    """Delete."""
    typer.echo("Delete an org")


@app.command()
def update() -> None:
    """Update."""
    typer.echo("Update an org")


if __name__ == "__main__":  # pragma: no cover
    app()
