import csv
import sys
from datetime import datetime

def parse_tabula_csv(file):
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
        return complete_row

    reader = csv.reader(file)
    complete_row = [''] * 5
    for row in reader:
        assert len(row) == 5
        if row[0]:
            if complete_row[0]:
                yield convert_to_num_columns(complete_row)
            complete_row = row
        else:
            complete_row[1] += row[1]
            assert not (row[0] and row[2] and row[3] and row[4])
    else:
        # EOF case:
        yield convert_to_num_columns(complete_row)

if __name__ == '__main__':
    with open('tabula-12-13.csv', 'rb') as file:
        withdrawls = 0
        deposits = 0
        for _transaction in parse_tabula_csv(file):
            withdrawls += _transaction[2]
            deposits += _transaction[3]
            print(_transaction)
        print("-" + str(withdrawls) + " +" + str(deposits) + "=>" + str(deposits - withdrawls))
