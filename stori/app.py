import json
import csv

from decimal import *
from sendEmail import send
from proccessTransaction import proccessTransaction


def lambda_handler(event, context):

    with open('txns.csv') as csvfile:
        read_csv = csv.DictReader(csvfile, delimiter=',')
        transactions = {}
        transactions_data = []
        acumulators = {
            "average_debit_amount": Decimal(0),
            "average_credit_amount": Decimal(0),
            "count_debit": 0,
            "count_credit": 0,
            "total_balance": Decimal(0)
        }
        

        for transaction in read_csv:
            proccessTransaction(transaction, transactions, acumulators)        
        
        average_credit_amount = acumulators["average_credit_amount"]/acumulators["count_credit"]
        average_debit_amount = acumulators["average_debit_amount"]/acumulators["count_debit"]
        total_balance = acumulators["total_balance"]

        for key in transactions:
            transactions_data.append({
                "description": "Number of transactions in " + key,
                "count": transactions[key]
            })
    
        send({
            "total_balance": str(total_balance),
            "average_credit_amount": str(average_credit_amount),
            "average_debit_amount": str(average_debit_amount),
            "transactions": transactions_data})

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
