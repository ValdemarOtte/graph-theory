### Imports
# Standard library

# Third-party libraries
import pytest

# Local files
from graph_theory.utils.functions import read_csv
from graph_theory.exceptions import WrongExtension


class TestUtilsFunctions:
    def test_read_csv():
        pass

    def rest_read_csv_error(self, test_extension_wrong):
        """Test if function will not delete the .wrong file."""
        with pytest.raises(WrongExtension):
            read_csv(test_extension_wrong)