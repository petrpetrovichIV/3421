import requests
from bs4 import BeautifulSoup

query = input('You find:')
url = f'https://www.google.com/search?q={query}'
response = requests.get(url)

# 2. Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 3. Find all 'a' tags and print their 'href'
for link in soup.find_all('a'):
    href = link.get('href')
    if href:
        print(href)