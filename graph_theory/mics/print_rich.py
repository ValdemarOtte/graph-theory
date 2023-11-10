### Imports
# Standard library

# Third-party libraries
from rich.console import Console
from rich.table import Table

# Local files


def print_adjacency_matrix(matrix: dict) -> None:
    """
    Function to print adjacency matrix.

    Args:
        data: A dict with information about the adjacency matrix
    """
    table = Table(title="Adjacency Matrix")
    table.add_column(" ", justify="right")

    for key in matrix:
        table.add_column(key, justify="left")

    for key in matrix:
        row = [key, *list(map(str, matrix[key].values()))]
        table.add_row(*row)

    console = Console()
    console.print(table)
