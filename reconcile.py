import piecash
import yaml


class Config:
    """Reads and stores configuration from a YAML file.
    """
    def __init__(self, filename):
        self._load_from_file(filename)

    def _load_from_file(self, filename):
        """Parses the supplied yaml filename.
        """
        with open("files/accounts.yaml") as config_file:
            yaml_string = config_file.read()
            self._config_dict = yaml.load(yaml_string)


class Book:
    """The entire account GnuCash book.
    """
    def __init__(self, filename):
        self._load_book_from_file(filename)

    def _load_from_file(self, filename):
        """Opens and initializes the Gnucash file.
        """
        with piecash.open_book(filename, readonly=False) as piecash_book:
            self._piecash_book = piecash_book


if __name__ == '__main__':
    # TODO make these command line arguments
    CONFIG_FILENAME = 'files/accounts.yaml'
    ACCOUNTS_FILENAME = 'files/accounts.gnucash'

    config = Config(filename=CONFIG_FILENAME)
    book = Book(filename=ACCOUNTS_FILENAME)

            imbalance_account = book.accounts[-1]
            split = imbalance_account.splits[0]
            split.account = book.accounts.get(name='Income')
            book.save()
