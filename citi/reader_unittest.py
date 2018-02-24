from StringIO import StringIO
import unittest
import textwrap

# import citibank statement reader
import reader

class ReaderUnitTest(unittest.TestCase):
    def test_trasaction_per_line(self):
        single_line_transactions = StringIO(textwrap.dedent(
            """
            12/06/2100, Hello World Transaction, 100, 0, 10100
            """
        ).lstrip())

        transaction_list = reader.parse_tabula_csv(single_line_transactions)
        for transaction in transaction_list:
            self.assertIsInstance(transaction, list)

if __name__ == '__main__':
    unittest.main()
