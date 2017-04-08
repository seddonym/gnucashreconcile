from app.commandhandler import CommandHandler


if __name__ == '__main__':
    CommandHandler().run()
    # TODO make these command line arguments
#     CONFIG_FILENAME = 'files/accounts.yaml'
#     ACCOUNTS_FILENAME = 'files/accounts.gnucash'
# 
#     config = Config(filename=CONFIG_FILENAME)
#     book = Book(filename=ACCOUNTS_FILENAME)
# 
#             imbalance_account = book.accounts[-1]
#             split = imbalance_account.splits[0]
#             split.account = book.accounts.get(name='Income')
#             book.save()
