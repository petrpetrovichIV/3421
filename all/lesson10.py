import requests
import sqlite3
import datetime
import time

connection = sqlite3.connect('currencies.sl3')
cursor = connection.cursor()
crypto_list = []

def str2price(price:str):
    return float(price[1:].replace(',',''))

def get_data():
    global crypto_list
    crypto_list = []
    response_text = requests.get('https://coinmarketcap.com/').text
    parse_elements = response_text.split('<span>')

    for element in parse_elements:
        if element.startswith('$'):
            for inner in element.split('</span>'):
                if inner.startswith('$'):
                    crypto_list.append(inner)
# ================================================================
def save_data():
    cursor.execute(f"""
        insert into prices (Name_currency, price, In_currency, updated_at)
        values ('BitCoin', {str2price(crypto_list[1])}, 'USD', '{datetime.datetime.now()}');
    """)
    connection.commit()
    #
    cursor.execute("select * from prices ORDER BY ROWID DESC LIMIT 1")
    connection.commit()
    prices = cursor.fetchall()
    for price in prices:
        print(price)

while True:
    get_data()
    save_data()
    time.sleep(10)



