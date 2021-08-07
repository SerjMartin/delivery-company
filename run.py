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
    print("Please enter the parcels number	expected for tomorrow")
    print("The number should be > 10 and <= 2000\n")

    data_str = input("Enter your data here:")
    #  print(f"The numbers of parsels is {data_str}")

    validate_parcel_number(data_str)


def validate_parcel_number(values):
    """
     Raises ValueErrror if the number is smaller than 10 or bigger than 2000.
    """
    try:
        if int(values) <= 10:
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


get_parcels_number()
