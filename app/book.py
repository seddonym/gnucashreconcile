import piecash

class Transaction:
    #def __init__(self, piecash_transaction):
    #    self._piecash_transaction = piecash_transaction
    # TODO - use a piecash transaction instead
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount


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
