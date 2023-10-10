import json
import csv

from decimal import *
from sendEmail import send


def lambda_handler(event, context):

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

    with open('txns.csv') as csvfile:
        read_csv = csv.DictReader(csvfile, delimiter=',')
        transactions = {}
        total_balance = Decimal(0)
        average_debit_amount = Decimal(0)
        average_credit_amount = Decimal(0)
        count_debit = 0
        count_credit = 0
        transactions_data = []

        for transaction in read_csv:

            date = transaction['Date'].split('/')
            transaction = Decimal(transaction['Transaction'])
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
        
        average_credit_amount = average_credit_amount/count_credit
        average_debit_amount = average_debit_amount/count_debit

        for key in transactions:
            transactions_data.append({
                "month": "Number of transactions in " + key,
                "count": transactions[key]
            })

        transactions = transactions_data
    
        send({
            "total_balance": str(total_balance),
            "average_credit_amount": str(average_credit_amount),
            "average_debit_amount": str(average_debit_amount),
            "transactions": transactions})

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Email sent successfully!",
            "total_balance": str(total_balance),
            "average_credit_amount": str(average_credit_amount),
            "average_debit_amount": str(average_debit_amount),
            "transactions": json.dumps(transactions)
        }),
    }
