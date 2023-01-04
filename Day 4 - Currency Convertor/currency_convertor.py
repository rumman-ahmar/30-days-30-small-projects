# pip install forex_python  to install the library

from forex_python.converter import CurrencyRates

cr = CurrencyRates()

amount = int(input("Please enter the amount: "))

from_currency = input("Please enter the currency code "
                      "that has to be converted: ").upper()

to_currency = input("Please enter the currency code "
                    "in which you want to convert: ").upper()

print(f"You are converting {amount} {from_currency} to {to_currency}")

converted_amount = cr.convert(from_currency, to_currency, amount)

print(f"The converted amount is: {converted_amount} {to_currency}")
