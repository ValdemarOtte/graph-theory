### Imports
# Standard library
import csv
from pathlib import Path

# Third-party libraries
# Local files
from graph_theory.exceptions import WrongExtensionError


def read_csv(path: Path) -> list[str]:
    """
    Read a csv-file.

    Returns it's content without the header.

    :param (Path) path: Path to csv-file
    :return:
    :raise WrongExtensionError: If the given path is not a csv-file.
    """
    if path.suffix != ".csv":
        raise WrongExtensionError
    with Path.open(path) as file:
        return list(csv.reader(file, delimiter=";"))[1:]
