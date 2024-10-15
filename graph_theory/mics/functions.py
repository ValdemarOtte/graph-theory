### Imports
# Standard library
import csv
from pathlib import Path

# Third-party libraries

# Local files


def read_csv(path: Path) -> list[str]:
    """
    Read a csv-file.
    
    Returns it's content without the header.

    :param (Path) path: Path to csv-file
    :return: 
    
    """
    with open(path) as file:
        return [row for row in csv.reader(file, delimiter=";")][1:]

