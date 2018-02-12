import csv
import sys

def parse_tabula_csv(file):
    reader = csv.reader(file)
    complete_row = [''] * 5
    for row in reader:
        assert len(row) == 5
        if row[0]:
            if complete_row[0]:
                # convert to float from string
                complete_row[2] = float(complete_row[2]) if complete_row[2] else 0
                complete_row[3] = float(complete_row[3]) if complete_row[3] else 0
                complete_row[4] = float(complete_row[4]) if complete_row[4] else 0
                yield complete_row
            complete_row = row
        else:
            complete_row[1] += row[1]

if __name__ == '__main__':
    with open('tabula-13-14.csv', 'rb') as file:
        withdrawls = 0
        deposits = 0
        for _transaction in parse_tabula_csv(file):
            withdrawls += _transaction[2]
            deposits += _transaction[3]
            print(_transaction)
        print("-" + str(withdrawls) + " +" + str(deposits) + "=>" + str(deposits - withdrawls))
