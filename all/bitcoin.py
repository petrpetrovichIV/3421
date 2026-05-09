import sqlite3
import datetime
import requests

connection = sqlite3.connect("db.sl3")
cursor = connection.cursor()

# cursor.execute("""
#     create table currencies_prices (
#         ID integer PRIMARY KEY,
#         currency text,
#         price real,
#         date_time text
#     );
# """)
# connection.commit()

def str_price_float(price: str):
    return float(price[1:].replace(',',''))

response_text = requests.get('https://coinmarketcap.com/').text
parse_elements = response_text.split('<span>')

list_currencies = []

for element in parse_elements:
    if element.startswith('$'):
        for inner in element.split('</span>'):
            if inner.startswith('$'):
                list_currencies.append(inner)

print(list_currencies)

# data = requests.get('https://api.monobank.ua/bank/currency').json()
# currency = 'USD'
# price = data[0]["rateSell"]
# # price = str_price_float(list_currencies[1])
#
# cursor.execute(f"""
#     insert into currencies_prices
#         (currency, price, date_time) values
#         ('{currency}', {price},'{datetime.datetime.now()}');
# """)
# connection.commit()
#
# cursor.execute("select * from currencies_prices;")
# connection.commit()
# prices = cursor.fetchall()
# for price in prices:
#     print(price)
#
# connection.close()