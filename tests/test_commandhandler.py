from unittest import TestCase
import os
from unittest.mock import Mock, patch, call
import sys
from app.commandhandler import CommandHandler


class TestCommandHandler(TestCase):
    def test_success(self):
        """Test a successful run of the entire command.
        """
        # Use a real file for the config
        CONFIG_FILENAME = os.path.join(
            os.path.dirname(__file__), 'files', 'config.yaml'
        )
        # Mock the book, so we don't have to interface with a Gnucash file 
        BOOK_FILENAME = 'path/to/foo_book_filename.gnucash'
        book = Mock()
        # book.get_unresolved_accounts.return_value = 

        USER_INPUTS = [
            'y',  # Accepting suggestions
        ]        
        command_handler = CommandHandler()
        
        
        with patch('app.commandhandler.Book') as mock_book_cls:
            mock_book_cls.return_value = book
            with patch('builtins.input', side_effect=USER_INPUTS) as mock_input:
                with patch.object(command_handler, 'print_message') as mock_print:
                    # Spoof passing command line arguments in
                    sys.argv.extend([CONFIG_FILENAME, BOOK_FILENAME])
                    command_handler.run()

        mock_book_cls.assert_called_once_with(filename=BOOK_FILENAME)
        
        mock_input.assert_has_calls([
            call('Accept these suggestions? (y/n): '),
        ])
        mock_print.assert_has_calls([
            call('Suggestions for unresolved transactions:'),
            call('Date\tDescription\tAmount\tDebit\tCredit'),
            call('19/03/2017\tCASH 19 MAR\t£30.00\tAssets.Current Account\tExpenses.Groceries'),
            call('21/03/2017\tMonthly Salary\t£1,500.00\tIncome.Salary\tAssets.Current Account'),
            call('Saved.'),
        ])
