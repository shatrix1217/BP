from bs4 import BeautifulSoup
import requests
import csv
import time

source = requests.get('https://www.bloomberg.com/asia').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('bloomberg_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'abstract'])

for article in soup.find_all('section'):
    headline = article.h2.a.text
    print(headline)

    abstract = article.find('div', class_='single-story-module__summary').p.text
    print(abstract)

    print()

    csv_writer.writerow([headline, abstract])

    time.sleep(2)

csv_file.close()