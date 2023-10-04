import csv
from decimal import *

print ("Stori Excersise")

months = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10':'October',
    '11':'November',
    '12':'December'
}

transactions = {};

with open('txns.csv') as csvfile:
    read_csv = csv.reader(csvfile, delimiter=',')
    line_count = 0
    total_balance = Decimal(0)
    average_debit_amount = Decimal(0)
    average_credit_amount = Decimal(0)
    count_debit = 0
    count_credit = 0
    for row in read_csv:
        if line_count > 0:
            date = row[1].split('/')
            transaction = Decimal(row[2])
            month = months[date[0]]
            value = transactions.get(month)
            if (value):
                transactions[month] = value + 1
            else:
                transactions[month] = 1
            if (transaction < 0):
                average_debit_amount += transaction
                count_debit += 1
            else:
                average_credit_amount += transaction
                count_credit += 1
            total_balance += transaction
        line_count += 1
    
    print(total_balance)
    print(average_credit_amount/count_credit)
    print(average_debit_amount/count_debit)
    print(transactions)