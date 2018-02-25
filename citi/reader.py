import csv
import sys
from datetime import datetime

from transaction import Transaction

def parse_tabula_csv(reader):
    """
    Parses the given citi bank debitcard statement CSV converted using tabula

    Format: Date, Transaction Details, Withdrawl, Deposit, Balance

    Sometimes `Transaction Details` may span accross multiple rows, but other
    fields would be empty.

    """
    def convert_to_num_columns(complete_row):
        # convert to float from string
        complete_row[0] = datetime.strptime(complete_row[0], '%d/%m/%Y')
        complete_row[2] = float(complete_row[2]) if complete_row[2] else 0
        complete_row[3] = float(complete_row[3]) if complete_row[3] else 0
        complete_row[4] = float(complete_row[4]) if complete_row[4] else 0
        return Transaction(date=complete_row[0],
                           description=complete_row[1],
                           withdrawl = complete_row[2],
                           deposit = complete_row[3],
                           balance = complete_row[4])

    complete_row = [''] * 5
    for row in reader:
        assert len(row) == 5
        if row[0]:
            if complete_row[0]:
                yield convert_to_num_columns(complete_row)
            complete_row = list(row)
        else:
            complete_row[1] += row[1]
            assert not (row[0] and row[2] and row[3] and row[4])
    else:
        # EOF case:
        yield convert_to_num_columns(complete_row)
