from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import re
import time
import csv
import os

options = webdriver.FirefoxOptions()
options.add_argument(
    '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/91.0.4472.124 Safari/537.36')
current_directory = "P:\\Paul\\Mike\\tripadvisor\\2. Output 1 - links"  # change to directory with links
relative_path = 'links_nice_clean.csv'  # change file name
csv_file_path = os.path.join(current_directory, relative_path)


def read_csv(file):
    with open(file, mode='r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data_list.extend(row)


def save_record(record):
    with open("test_nice.csv", "a+", encoding="UTF-8", newline="") as file:  # change output file name
        columns = list(record.keys())
        fieldnames = [i for i in columns]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(record)


def get_data(hotel):
    # variables
    print("\nGetting Data")
    record = {}
    amenities = []

    # page data
    driver = webdriver.Firefox(options=options)
    url = "https://www.tripadvisor.de/" + hotel
    driver.get(url)
    print(url)
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # hotel link
    hotel = hotel.split('-')
    geo = hotel[1]
    loc = hotel[2]
    hotel = geo + loc
    print(hotel)
    record["url"] = hotel

    # adress
    try:
        adress = soup.find('span', class_='fHvkI PTrfg').text
    except:
        adress = False
        print("No adress")
    if adress:
        record["Adress"] = adress
    else:
        record['Adress'] = "No adress available"

    # stars
    elements_with_aria_label = soup.find_all(attrs={'aria-label': True})
    record['Stars'] = "No stars available"
    for element in elements_with_aria_label:
        aria_label = element['aria-label']
        if aria_label.endswith('Sternen'):  # change word according to language (if EN website, then use "Stars")
            record['Stars'] = aria_label[0:3]
            break

    # price
    try:
        prices = []
        price = soup.find_all(attrs={"data-automation": True})
        price_pattern = re.compile(r'(\d+)€')
        for element in price:
            if "€" in element.get_text():
                text = element.get_text()
                match = re.search(price_pattern, text)
                if match:
                    prices.append(match.group(1))
        int_values = [int(x) for x in prices]
        average_price = sum(int_values) / len(int_values) if len(int_values) > 0 else False
        print("AVG Price:", average_price)
    except:
        average_price = False
        print("No price found")
    if average_price:
        record["Price on Scrape Date"] = round(average_price, 2)
    else:
        record['Price on Scrape Date'] = "No price available"

    # amenities
    amenities = soup.find_all(attrs={'data-test-target': 'amenity_text'})
    for el in amenities:
        record[el.text] = el.text

    driver.quit()
    print("Done")
    return record


if __name__ == "__main__":
    data_list = []
    read_csv("links_naples.csv")  # use csv_file_path
    for hotel in data_list:
        data = get_data(hotel)
        save_record(data)