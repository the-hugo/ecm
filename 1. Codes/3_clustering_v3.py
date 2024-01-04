from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time
import csv
import os
import re

options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('window-size=1920x1080')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
ua = UserAgent()
user_agent = ua.random
options.add_argument(f'user-agent={user_agent}')
current_directory = "P:\\Paul\\Mike\\tripadvisor\\2. Output 1 - links" # change to directory with links
relative_path = 'links_nice_clean.csv' # change file name
csv_file_path = os.path.join(current_directory, relative_path)

def read_csv(file):
    with open(file, mode='r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data_list.extend(row)


def save_record(record):
    with open("clustering_nice_v2.csv", "a+", encoding="UTF-8", newline="") as file: # change output file name
        fieldnames = ["ID", "Adresse", "Sterne", "Amenities"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(record)


def get_data(hotel):
    print("\nGetting Data")
    url = hotel.split('-')

    record = {
        "ID": url[2],
        "Adresse": "NA",
        "Sterne": "NA",
        "Amenities": "NA"
    }

    amenities = []
    driver = webdriver.Chrome(options=options)
    url = "https://www.tripadvisor.de/"+hotel
    driver.get(url)
    print(url)

    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(10)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    """
    try:
        price_tag = soup.find('div', class_='JPNOn JPNOn').text
    except:
        print("No price found")
    """
    adress = soup.find('span', class_='fHvkI PTrfg')
    if adress is None:
        print("Trying alternative")
        adress = soup.find_all('span', class_='biGQs _P pZUbB KxBGd')
        for i in adress:
            label = i.text
            if "Nizza" in label:
                record["Adresse"] = label
                print("+")
                break
    else:
        print("*")
        record["Adresse"] = adress.text

    amenities = soup.find_all(attrs={'data-test-target': 'amenity_text'})
    elements_with_aria_label = soup.find_all(attrs={'aria-label': True})

    for element in elements_with_aria_label:
        aria_label = element['aria-label']
        if aria_label.endswith('Sternen'): # change word according to language
            record['Sterne'] = aria_label[0:3]
    amenities_s = [i.text for i in amenities]
    record["Amenities"] = amenities_s
    """
    try:
        record["Adress"] = adress
        record["Price on Scrape Date"] = price_tag
    except:
        pass
    """
    driver.quit()
    if record["Adresse"] == "NA":
        print("No Adress")
    print("Done")
    return record

if __name__ == "__main__":
    data_list = []
    read_csv(csv_file_path) # use csv_file_path
    for hotel in data_list:
        data = get_data(hotel)
        save_record(data)