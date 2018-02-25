import unittest
import textwrap
import sys

# to allow transcation.py
sys.path.insert(0, '.')
# import citibank statement reader
from citi import reader
from transaction import Transaction

class ReaderUnitTest(unittest.TestCase):
    def test_trasaction_per_line(self):
        single_line_transactions = [
                ['12/06/2100', 'Hello World Transaction', '100', '0', '10100'],
        ]

        transaction_list = reader.parse_tabula_csv(single_line_transactions)
        count = 0
        for transaction in transaction_list:
            count += 1
            self.assertIsInstance(transaction, Transaction)
            self.assertEquals(100, transaction.withdrawl)
            self.assertEquals(10100, transaction.balance)
            self.assertTrue(transaction.description.startswith('Hello'))
        self.assertEquals(1, count)

    def test_trasaction_multi_line(self):
        multi_line_transactions = [
                ['12/06/2100', 'Hello World Transaction', '100', '0', '10100'],
                ['', ' from 2nd', '', '', ''],
                ['', ' from 3rd', '', '', ''],
                ['', ' from 4th', '', '', ''],
        ]

        transaction_list = reader.parse_tabula_csv(multi_line_transactions)
        count = 0
        for transaction in transaction_list:
            count += 1
            self.assertIsInstance(transaction, Transaction)
            self.assertEquals(100, transaction.withdrawl)
            self.assertEquals(10100, transaction.balance)
            self.assertEquals(multi_line_transactions[0][1] +
                              multi_line_transactions[1][1] +
                              multi_line_transactions[2][1] +
                              multi_line_transactions[3][1] ,
                              transaction.description
            )
        self.assertEquals(1, count)

if __name__ == '__main__':
    unittest.main()
