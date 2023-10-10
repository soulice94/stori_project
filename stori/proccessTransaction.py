from decimal import *

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

def proccessTransaction(transaction, transactions, acumulators):

    date = transaction['Date'].split('/')
    decimal_transaction = Decimal(transaction['Transaction'])

    month = months[date[0]]
    value = transactions.get(month)
    if (value):
        transactions[month] = value + 1
    else:
        transactions[month] = 1
    if (decimal_transaction < 0):
        acumulators["average_debit_amount"] += decimal_transaction
        acumulators["count_debit"] += 1
    else:
        acumulators["average_credit_amount"] += decimal_transaction
        acumulators["count_credit"] += 1
    
    acumulators["total_balance"] += decimal_transaction
