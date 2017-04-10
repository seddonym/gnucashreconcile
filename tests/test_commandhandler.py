from unittest import TestCase
from unittest.mock import Mock, patch, call
import sys
from app.commandhandler import CommandHandler


class TestCommandHandler(TestCase):
    def test_success(self):
        """Test a successful run of the entire command.
        """
        CONFIG_FILENAME = 'path/to/bar_book_filename.yaml'
        BOOK_FILENAME = 'path/to/foo_book_filename.gnucash'
        
        with patch('app.commandhandler.Book') as mock_book_cls:
            with patch('builtins.input', side_effect=['y']) as mock_input:
                with patch('builtins.print') as mock_print:
                    # Spoof passing command line arguments in
                    sys.argv.extend([CONFIG_FILENAME, BOOK_FILENAME])
                    CommandHandler().run()

        mock_book_cls.assert_called_once_with(filename=BOOK_FILENAME)

        mock_print.assert_has_calls([
            call('Suggestions: []'),
            call('Saved.'),
        ])
