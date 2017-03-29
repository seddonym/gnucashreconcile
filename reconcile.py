import piecash

with piecash.open_book("files/accounts.gnucash", readonly=False) as book:
    # get default currency of book
    imbalance_account = book.accounts[-1]
    split = imbalance_account.splits[0]
    split.account = book.accounts.get(name='Income')
    book.save()
