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
    :returns:
    :raise WrongExtensionError: If the given path is not a csv-file.
    """
    if path.suffix != ".csv":
        raise WrongExtensionError
    with Path.open(path) as file:
        return list(csv.reader(file, delimiter=";"))[1:]


def merge_dict_to_tabel(data: list[dict], labels: list[str]) -> list[list]:
    """
    Merge dict together to one tabel.
    
    :param (list[dict]) data: Dictionaries with the data.
    :param (list[str]) labels: The labels over data.
    :returns (list[list]) merge_data: The merge data.    
    """
    merge_data: list = []
    merge_data.append(["Edge"] + labels)
    for i, key in enumerate(data[0].keys(), start=1):
        merge_data.append([key])
        for element in data:
            merge_data[i].append(str(element[key]))
    return merge_data


def print_tabel(data: list[list]):
    
    lenght: list = [0 for _ in data[0]]
    for row in data:
        for i, element in enumerate(row):
            if len(element) > lenght[i]:
                lenght[i] = len(element)
    
    for i, row in enumerate(data):
        print(" | ".join(row))


if __name__ == "__main__":
    level = {'I': 0, 'C': 1, 'M': 1, 'A': 2, 'D': 2, 'G': 2, 'H': 2, 'J': 2, 'B': 3, 'E': 3, 'L': 3, 'F': 3, 'K': 3}    
    time = {'I': 1, 'C': 2, 'M': 3, 'A': 4, 'D': 5, 'G': 6, 'H': 7, 'J': 8, 'B': 9, 'E': 10, 'L': 11, 'F': 12, 'K': 13}
    data = [level, time]
    labels = ["level", "time"]
    merge_data = merge_dict_to_tabel(data, labels)
    print_tabel(merge_data)
    