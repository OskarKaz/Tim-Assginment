import requests
import json

currency_owned = input("Enter the currency which you have: ")

if currency_owned.isnumeric():
    print("Error! Invalid input!")
    currency_owned = input("Enter the currency which you have: ")

convert_currency = input("Enter the currency you would like to change: ")

while convert_currency.isnumeric():
    print("Error! Invalid input!")
    convert_to_currency = input("Enter the currency you would like to change: ")


response = requests.get(
    f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{currency_owned}/{convert_currency}.min.json'
)

if response.status_code != 200:
    print(f"Your access has been denied! [{response.status_code}]")
    quit()

print(f"You have sucessfully connected! [{response.status_code}]")
current_rate = response.json()[convert_currency]

print(f"The current exchange rate you requested is: {current_rate} {currency_owned.upper()} to {convert_currency.upper()}")

amount_to_exchange: int = int(input("Enter the amount that you would like to exchange: "))

print(f"The amount of {convert_currency.upper()} you will receive is {amount_to_exchange * current_rate}")