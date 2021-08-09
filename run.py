import gspread
#  Import the gspread library.
from google.oauth2.service_account import Credentials
# Import the Credentials class from google auth.

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
# The scop lists the APIs that the program will access to runs.

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('delivery_company')
#  These settings are to access spreadsheet data.


def get_parcels_number():
    """
     Get parcels numbers from central depo.
    """
    while True:
        """
         While loop will continue until the input data
         will be valid for 10 drivers.
        """

        print("Please enter the parcels number")
        print("The number should be > 10 and <= 2000\n")

        data_str = input("Enter your data here:\n")

        if validate_parcel_number(data_str):
            print("Data is valid")
            break
    return data_str


def validate_parcel_number(values):
    """
     Raises ValueErrror if the number is smaller than 10 or bigger than 2000.
    """
    try:
        if int(values) < 10:
            raise ValueError(
                f"{values} and is not enough for your 10 drivers!"
            )
        elif int(values) > 2000:
            raise ValueError(
                f"{values}.\nYou need {round(int(values) / 200)}"
                " dirvers for tomorrow"
            )
    except ValueError as e:
        print(f"Warning!\nThe number of parcels is {e}\n")
        return False
    return True


def parcels_per_driver(parcels):
    """
     Calculate how many parcels per driver and update the spreadsheet.
    """
    headings = SHEET.worksheet("parcels").get_all_values()[0]
    # print(headings)
    per_day_parcels = round(int(parcels) / int(len(headings)))
    print(f"Every driver got per day:{per_day_parcels} parcels.")

    row = []
    for x in range(len(headings)):
        x = per_day_parcels
        row.append(x)
    # print(row)
    return row


def update_parcels_worksheet(quantity):
    """
     Update parcels worksheet, add a new row with the number
      of parcels per driver
    """
    print("Updating parcels worksheet...\n")
    parcels_worksheet = SHEET.worksheet("parcels")
    parcels_worksheet.append_row(quantity)
    print("Parcels woeksheet updated successfuly.\n")


def get_hours(parcels):
    """
     Calculate how many hours per day.
    """
    headings = SHEET.worksheet("hours").get_all_values()[0]
    hours_per_day = round(int(parcels) / int(len(headings)) / 30) + 1
    # One driver can do 30 parcel per hour + 1 hour for break

    print(f"Every driver worked:{hours_per_day} hour.")

    row = []
    for x in range(len(headings)):
        x = hours_per_day
        row.append(x)
    # print(row)
    return row


def update_hours_worksheet(hours):
    """
     Update hours worksheet, add a new row with the hours.
    """
    print("Updating hours worksheet...\n")
    hours_worksheet = SHEET.worksheet("hours")
    hours_worksheet.append_row(hours)
    print("Hours woeksheet updated successfuly.\n")


def get_salary(hours):
    """
     Calculate salary per day.
    """
    headings = SHEET.worksheet("salary").get_all_values()[0]
    salary_per_day = round(int(parcels) / int(len(headings)) / 30) * 12
    # Driver get 12 € per hour

    print(f"For every driver you pay:{salary_per_day} euro")

    row = []
    for x in range(len(headings)):
        x = salary_per_day
        row.append(x)
    # print(row)
    return row


def update_salary_worksheet(salary):
    """
     Update salary worksheet, add a new row with the number
      of parcels per driver
    """
    print("Updating salary worksheet...\n")
    salary_worksheet = SHEET.worksheet("salary")
    salary_worksheet.append_row(salary)
    print("Salary worksheet updated successfuly.\n")


def get_profit(hours):
    """
     Calculate full payment for all drivers
     and your profit
    """
    headings = SHEET.worksheet("salary").get_all_values()[0]
    salary_per_day = round(int(parcels) / int(len(headings)) / 30) * 12
    # Driver get 12 € per hour

    full_paymant = salary_per_day * len(headings)
    print(f"You paid to drivers:{full_paymant} euro.")
    # print(full_paymant)
    full_profit = int(parcels) * 5 - int(full_paymant)
    # Delivery company charging 5 € per parcel for service
    # print(full_profit)
    print(f"Your profit is: {full_profit} euro.")
    headings = SHEET.worksheet("profit").get_all_values()[0]
    row = []
    for x in range(len(headings)):
        x = full_profit
        row.append(x)

    return row


def update_profit_worksheet(profit):
    """
     Update profit worksheet, add a new row with the profit.
    """

    print("Updating profit worksheet...\n")
    profit_worksheet = SHEET.worksheet("profit")
    profit_worksheet.append_row(profit)
    print("Profit worksheet updated successfuly.\n")


parcels = get_parcels_number()
quantity = parcels_per_driver(parcels)
update_parcels_worksheet(quantity)
hours = get_hours(parcels)
update_hours_worksheet(hours)
salary = get_salary(hours)
update_salary_worksheet(salary)
profit = get_profit(hours)
update_profit_worksheet(profit)


print("Welcome to delivery company data automation")
