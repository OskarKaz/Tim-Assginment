import json
import requests

response = requests.get(f"https://v6.exchangerate-api.com/v6/cfdfcd38a3755b9aaf265c8a/latest/USD")

print("Please enter your currency that you would like to convert:")
starting_currency = str(input())

while starting_currency.isnumeric():
    print("Sorry invalid input")
    print("Please enter your currency that you would like to convert:")
    starting_currency = str(input())


print("Please enter the currency that you would like to change to:")
Converted_Currency = str(input())

while Converted_Currency.isnumeric():
    print("Sorry invalid input")
    print("Please enter the currency that you would like to change to:")
    Converted_Currency = str(input())


if response.status_code == 200:
    print("You have sucessfully connected")
else:
    print("Your access has been denied, please try again")



print(response.status_code)



   