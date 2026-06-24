import typer
import json
from pathlib import Path
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()

def load(path: str) -> dict:
    return json.loads(Path(path).read_text())

def score(a: dict, b: dict) -> tuple[int, int, int]:
    keys = set(a) | set(b)
    improved = regressions = unchanged = 0
    for k in keys:
        av, bv = a.get(k), b.get(k)
        if av == bv:
            unchanged += 1
        elif bv is not None and av is not None and str(bv) > str(av):
            improved += 1
        else:
            regressions += 1
    return improved, regressions, unchanged

@app.command()
def diff(
    run_a: str = typer.Argument(..., help="Baseline eval run (JSON)"),
    run_b: str = typer.Argument(..., help="Candidate eval run (JSON)"),
    json_out: bool = typer.Option(False, "--json", help="Machine-readable output"),
):
    """Diff two LLM eval runs and score the delta."""
    a, b = load(run_a), load(run_b)
    improved, regressions, unchanged = score(a, b)

    if json_out:
        print(json.dumps({"improved": improved, "regressions": regressions, "unchanged": unchanged}))
        return

    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_row("▲ improved",   f"[green]{improved}[/green]")
    table.add_row("▼ regressions", f"[red]{regressions}[/red]")
    table.add_row("● unchanged",  f"[dim]{unchanged}[/dim]")
    console.print(table)

if __name__ == "__main__":
    app()
