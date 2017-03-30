import piecash
import yaml

if __name__ == '__main__':
    with open("files/accounts.yaml") as config_file:
        yaml_string = config_file.read()
        match_config = yaml.load(yaml_string)

    with piecash.open_book("files/accounts.gnucash", readonly=False) as book:
        # get default currency of book
        imbalance_account = book.accounts[-1]
        split = imbalance_account.splits[0]
        split.account = book.accounts.get(name='Income')
        book.save()
