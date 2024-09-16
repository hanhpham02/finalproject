# libraries, packages, modules
import csv # to store transactions in a csv file
import pandas as pd
from tabulate import tabulate # table frame
import re #regex

# ask user what they want to do
def main():
    print("What you want to do?")
    print("(1) - add transactions")
    print("(2) - view total income")
    print("(3) - view total expenses")
    print("(4) - view savings")
    print("(5) - view transaction history")

    while True:
        try:
            button = int(input("Click: ")) # only 1 - 5
            if button not in [1, 2, 3, 4, 5]:
                continue
            else:
                break
        except ValueError:
            pass

    if button == 1:
        trans()

    if button == 2:
        while True:
            start_date = input("Start date: ")
            if re.search(r"^[0-9]{4}\-(0[1-9]|1[0-2])\-(0[1-9]|[1-2][0-9]|3[0-1])$", start_date):
                break
        while True:
            end_date = input("End_date: ")
            if re.search(r"^[0-9]{4}\-(0[1-9]|1[0-2])\-(0[1-9]|[1-2][0-9]|3[0-1])$", end_date):
                break     
        print(income(start_date, end_date))

    if button == 3:
        while True:
            start_date = input("Start date: ")
            if re.search(r"^[0-9]{4}\-(0[1-9]|1[0-2])\-(0[1-9]|[1-2][0-9]|3[0-1])$", start_date):
                break
        while True:
            end_date = input("End_date: ")
            if re.search(r"^[0-9]{4}\-(0[1-9]|1[0-2])\-(0[1-9]|[1-2][0-9]|3[0-1])$", end_date):
                break     
        print(expenses(start_date, end_date))

    if button == 4:
        while True:
            start_date = input("Start date: ")
            if re.search(r"^[0-9]{4}\-(0[1-9]|1[0-2])\-(0[1-9]|[1-2][0-9]|3[0-1])$", start_date):
                break
        while True:
            end_date = input("End_date: ")
            if re.search(r"^[0-9]{4}\-(0[1-9]|1[0-2])\-(0[1-9]|[1-2][0-9]|3[0-1])$", end_date):
                break     
        print(savings(start_date, end_date))

    if button == 5:
        his()

# user input date YYYY-MM-DD, amount, description to a CSV file
def trans():
    while True:
        try:
            while True:
                date = input("Date (YYYY-MM-DD): ")
                if re.search(r"^[0-9]{4}\-(0[1-9]|1[0-2])\-(0[1-9]|[1-2][0-9]|3[0-1])$", date):
                    break
            while True:
                amount = input("Amount: ")
                if re.search(r"^\-?\d+$", amount):
                    break
            description = input("Description: ")

            with open("transactions.csv", "a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow([date, amount, description])
        except EOFError:
            break

def his():
    column_names = ['Date', 'Amount', 'Description'] # Define the column names
    df = pd.read_csv('transactions.csv', header=None, names=column_names) #data frame
    df['Date'] = pd.to_datetime(df['Date']) #convert to datetime data type
    while True:
            start_date = input("Start date: ")
            if re.search(r"^[0-9]{4}\-(0[1-9]|1[0-2])\-(0[1-9]|[1-2][0-9]|3[0-1])$", start_date):
                break
    while True:
        end_date = input("End_date: ")
        if re.search(r"^[0-9]{4}\-(0[1-9]|1[0-2])\-(0[1-9]|[1-2][0-9]|3[0-1])$", end_date):
            break   
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)] #filter dates   
    while True:
        try:
            type_of_changes = int(input("Type: (1) Income (2) Expenses (3) Both: ")) # only 1 - 3
            if type_of_changes not in [1, 2, 3]:
                continue
            else:
                break
        except ValueError:
            pass
    if type_of_changes == 1:
        filtered_df = filtered_df[filtered_df['Amount'] > 0]
    if type_of_changes == 2:
        filtered_df = filtered_df[filtered_df['Amount'] < 0]
    filtered_df.to_csv('history.csv', index=False) #save to a new csv file
    # display table
    with open("history.csv") as file:
        reader = csv.reader(file)
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))

def income(start_date, end_date):
    column_names = ['Date', 'Amount', 'Description'] # Define the column names
    df = pd.read_csv('transactions.csv', header=None, names=column_names) #data frame
    df['Date'] = pd.to_datetime(df['Date']) #convert to datetime data type
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)] #filter dates
    filtered_df = filtered_df[filtered_df['Amount'] > 0]
    total_sum = filtered_df['Amount'].sum()
    return f"Your income from {start_date} to {end_date} is: {total_sum}"

def expenses(start_date, end_date):
    column_names = ['Date', 'Amount', 'Description'] # Define the column names
    df = pd.read_csv('transactions.csv', header=None, names=column_names) #data frame
    df['Date'] = pd.to_datetime(df['Date']) #convert to datetime data type
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)] #filter dates
    filtered_df = filtered_df[filtered_df['Amount'] < 0]
    total_sum = filtered_df['Amount'].sum()
    return f"Your expense from {start_date} to {end_date} is: {-total_sum}"

def savings(start_date, end_date):
    column_names = ['Date', 'Amount', 'Description'] # Define the column names
    df = pd.read_csv('transactions.csv', header=None, names=column_names) #data frame
    df['Date'] = pd.to_datetime(df['Date']) #convert to datetime data type
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)] #filter dates
    total_sum = filtered_df['Amount'].sum()
    if total_sum >= 0:
        return f"Your savings from {start_date} to {end_date} is: {total_sum}"
    else:
        return f"From {start_date} to {end_date}, you overspent: {-total_sum}"

if __name__ == "__main__":
    main()

# add new comment
# second comment
# third comment
