import requests

resp = requests.get("https://coinmarketcap.com/")

html = resp.text

html_parse = html.split('<span>')

crypto_list = []

for item in html_parse:
    if item.startswith('$'):
        for inner_item in item.split('</span>'):
            if inner_item.startswith('$'):
                crypto_list.append(inner_item)

print(crypto_list)

print(f'BitCoin: {crypto_list[1]}')

bit_coin_price = float(crypto_list[1][1:].replace(',',''))

count = int(input("How many? "))

print(f'${bit_coin_price*count}')

