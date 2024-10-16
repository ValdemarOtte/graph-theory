# Custom exceptions defined for use in pensumlist_scraper modules.


class GraphTheoryError(Exception):
    """Base class for Graph Theory errors."""


class WrongExtensionError(GraphTheoryError):
    """IF given extension is wrong."""
