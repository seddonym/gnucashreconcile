import piecash

 
class Book:
    """The entire account GnuCash book.
    """
    def __init__(self, filename):
        self._load_from_file(filename)
 
    def _load_from_file(self, filename):
        """Opens and initializes the Gnucash file.
        """
        with piecash.open_book(filename, readonly=False) as piecash_book:
            self._piecash_book = piecash_book
