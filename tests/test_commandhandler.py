from unittest import TestCase, skip
from unittest.mock import Mock, patch, call, sentinel
import os
import sys
from moneyed import Money, GBP
from datetime import date
from app.commandhandler import CommandHandler


class TestCommandHandler(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.command_handler = CommandHandler()
        
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
        suggestions = [
            Mock(date=date(2017, 3, 19),
                 description='CASH 19 MAR',
                 amount=Money(30, GBP),
                 debit_account='Assets.Current Account',
                 credit_account='Expenses.Groceries'
            ),
            Mock(date=date(2017, 3, 21),
                 description='Monthly Salary',
                 amount=Money(1500, GBP),
                 debit_account='Income.Salary',
                 credit_account='Assets.Current Account'
            ),
        ]

        USER_INPUTS = [
            'y',  # Accepting suggestions
        ]        
        
        with patch('builtins.input', side_effect=USER_INPUTS) as mock_input:
            with patch.object(self.command_handler, 'print_message') as mock_print:
                with patch.object(self.command_handler, 'get_suggestions', return_value=suggestions):
                    # Spoof passing command line arguments in
                    sys.argv.extend([CONFIG_FILENAME, BOOK_FILENAME])
                    
                    self.command_handler.run()

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
    
    @skip
    def test_run(self):
        assert False
        
    @skip
    def test_store_user_input(self):
        assert False
    
    @skip
    def test_get_suggestions(self):
        assert False
    
    def test_preview_suggestions(self):
        with patch.object(self.command_handler, 'get_suggestions',
                          return_value=sentinel.suggestions) as mock_get_suggestions:
            with patch.object(self.command_handler, 'render_suggestions') as mock_render_suggestions:
                self.command_handler.preview_suggestions()
        
        mock_get_suggestions.assert_called_once_with()
        self.assertEqual(self.command_handler.suggestions, sentinel.suggestions)
        mock_render_suggestions.assert_called_once_with()
    
    def test_render_suggestions(self):
        self.command_handler.suggestions = [
            Mock(date=date(2017, 3, 19),
                 description='CASH 19 MAR',
                 amount=Money(30, GBP),
                 debit_account='Assets.Current Account',
                 credit_account='Expenses.Groceries'
            ),
            Mock(date=date(2017, 3, 21),
                 description='Monthly Salary',
                 amount=Money(1500, GBP),
                 debit_account='Income.Salary',
                 credit_account='Assets.Current Account'
            ),
        ]
        with patch.object(self.command_handler, 'print_message') as mock_print:
            self.command_handler.render_suggestions()
        
        mock_print.assert_has_calls([
            call('Suggestions for unresolved transactions:'),
            call('Date\tDescription\tAmount\tDebit\tCredit'),
            call('19/03/2017\tCASH 19 MAR\t£30.00\tAssets.Current Account\tExpenses.Groceries'),
            call('21/03/2017\tMonthly Salary\t£1,500.00\tIncome.Salary\tAssets.Current Account'),
        ])
    
    @skip
    def test_save_suggestions(self):
        assert False
    
    @skip
    def test_get_matcher(self):
        assert False
    
    @skip
    def test_get_config(self):
        assert False
    
    @skip
    def test_get_book(self):
        with patch('app.commandhandler.Book') as mock_book_cls:
            mock_book_cls.return_value = book
            
            self.command_handler.get_book()

        BOOK_FILENAME = 'path/to/foo_book_filename.gnucash'
        mock_book_cls.assert_called_once_with(filename=BOOK_FILENAME)

    @skip
    def test_user_confirms(self):
        assert False


    def test_print_message(self):
        with patch('builtins.print') as mock_print:
            self.command_handler.print_message('Foo.')
        mock_print.assert_called_once_with('Foo.')
    
