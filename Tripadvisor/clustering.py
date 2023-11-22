import csv
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

# def read_csv(file):
#     with open(file, mode='r', newline='') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             data_list.extend(row)


def get_data():
    driver = webdriver.Chrome()
    driver.get("https://www.tripadvisor.de/Hotel_Review-g187791-d1729030-Reviews-IQ_Hotel_Roma-Rome_Lazio.html")
    time.sleep(3)
    elements = driver.find_elements(By.XPATH, "//div[@data-test-target='amenity_text']")
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.find_all(attrs={'data-test-target': 'amenity_text'})
    elements_with_aria_label = soup.find_all(attrs={'aria-label': True})
    div_element = soup.find('div', class_='CMiVw _R MC S4 _a H')
    # Filter elements where aria-label ends with "Sterne"
    for i in div_element:
        all_text = i.get_text(strip=True)
        print(all_text)
    for element in elements_with_aria_label:
        aria_label = element['aria-label']
        if aria_label.endswith('Sternen'):
            stars_text = aria_label
    for el in elements:
        print(el.text)
    driver.quit()


if __name__ == "__main__":
    """
    data_list = []
    read_csv("links_naples.csv") #  input file name
    for hotel in data_list:
        data = get_data(hotel)
    """
    data = get_data()