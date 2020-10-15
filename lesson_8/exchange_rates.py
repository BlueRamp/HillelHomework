import requests
currency_from = input("currency_from: ")
currency_to = input("currency_to: ")
amount = float(input("amount: "))
date = input("input date (in form year-month-day): ")
request = requests.get(f"https://api.exchangerate.host/convertfrom={currency_from}&to={ currency_to}&amount={amount}"
                       f"&date={date}")

exchange_rate = request.json()

# print(exchange_rate["rates"][currency_to])
print(["date", "from", "to", "amount", "rate", "result"], "\n",
      [date, currency_from, currency_to, amount, exchange_rate["rates"][currency_to],
       exchange_rate["rates"][currency_to]*amount])
