from argparse import ArgumentParser
import sys
from .config import Config
from .book import Book
from .matcher import Matcher


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
        self.print_message('Suggestions: {}'.format(self.suggestions))
    
    def save_suggestions(self):
        self.print_message('Saved.')
    
    def user_confirms(self):
        YES, NO = 'y', 'n'

        while True:
            user_input = input('Save matches? (y/n): ').lower()
            if user_input in [YES, NO]:
                break
            else:
                self.print_message('Please enter {} or {}.'.format(YES, NO))
        
        return user_input == YES
    
    def print_message(self, message):
        print(message)
        