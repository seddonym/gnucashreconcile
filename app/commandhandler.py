from argparse import ArgumentParser
import sys
from moneyed import GBP
from moneyed.localization import (format_money, _format as set_money_format,
                                  _sign as set_currency_sign)
from .config import Config
from .book import Book
from .matcher import Matcher
from decimal import ROUND_HALF_UP


set_money_format('en_GB', group_size=3, group_separator=",", decimal_point=".",
                 positive_sign="", trailing_positive_sign="",
                 negative_sign="-", trailing_negative_sign="",
                 rounding_method=ROUND_HALF_UP)
set_currency_sign('en_GB', GBP, prefix='£')


class CommandHandler:
    """Handles the user flow and display.
    """
    def run(self):
        self.store_user_input()
        self.preview_suggestions()
        if self.user_confirms():
            self.save_suggestions()
        else:
            self.print_message('Aborted.')

    def store_user_input(self):
        """Gets the config and book filenames from the command line, and stores them as
        attributes on this instance.
        """
        parser = ArgumentParser()
        parser.add_argument("config", help="The name of the .yml file that contains the matching configuration.")
        parser.add_argument("accounts", help="The name of the GnuCash file that contains the accounts.")
        
        args = parser.parse_args()
        
        self.config_filename = args.config
        self.book_filename = args.accounts

    def preview_suggestions(self):
        self.suggestions = self.get_suggestions()
        self.render_suggestions()
    
    def get_suggestions(self):
        return self.get_matcher().get_suggestions()
    
    def get_matcher(self):
        return Matcher(config=self.get_config(),
                       book=self.get_book())
    
    def get_config(self):
        return Config(filename=self.config_filename)
    
    def get_book(self):
        return Book(filename=self.book_filename)
    
    def render_suggestions(self):
        self.print_message('Suggestions for unresolved transactions:')
        self.print_message('Date\tDescription\tAmount\tDebit\tCredit')
        for suggestion in self.suggestions:
            parts = [str(part) for part in (
                suggestion.date.strftime('%d/%m/%Y'),
                suggestion.description,
                format_money(suggestion.amount, locale='en_GB'),
                suggestion.debit_account,
                suggestion.credit_account,
            )]
            self.print_message('\t'.join(parts))
    
    def save_suggestions(self):
        self.print_message('Saved.')
    
    def user_confirms(self):
        YES, NO = 'y', 'n'

        while True:
            user_input = input('Accept these suggestions? (y/n): ').lower()
            if user_input in [YES, NO]:
                break
            else:
                self.print_message('Please enter {} or {}.'.format(YES, NO))
        
        return user_input == YES
    
    def print_message(self, message):
        print(message)
        