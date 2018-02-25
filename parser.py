import csv
import sys

# to allow transcation.py
# sys.path.insert(0, '.')

import citi.reader as citi

if __name__ == '__main__':
    with open('tabula-12-13.csv', 'rb') as f:
        withdrawls = 0
        deposits = 0
        for _transaction in citi.parse_tabula_csv(csv.reader(f)):
            withdrawls += _transaction.withdrawl
            deposits += _transaction.deposit
            print(_transaction)
        print("-" + str(withdrawls) + " +" + str(deposits) + "=>" + str(deposits - withdrawls))
