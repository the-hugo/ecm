import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from bs4 import BeautifulSoup
import requests
import time
import csv

BASE_URL = 'https://www.tripadvisor.de/Hotels-g187791-Rome_Lazio-Hotels.html'
PER_PAGE = 30

def get_id_from_url(URL):
  # Split URL by -g to divide it before the ID
  prefix, suffix = URL.split('-g', maxsplit=1)
  # Divide the URL after the ID (first dash)
  id, slug = suffix.split('-', maxsplit=1)
  return int(id)

def get_listing_url(page, base_url=BASE_URL, per_page=PER_PAGE):
  assert page >= 0
  id = get_id_from_url(base_url)
  if page == 0:
    return BASE_URL

  return BASE_URL.replace(f'-g{id}-', f'-g{id}-oa{page * per_page}-')

def get_number_of_pages(BASE_URL, PER_PAGE):
    try:
        # Create a WebDriver instance (e.g., Chrome WebDriver)
        driver = webdriver.Chrome()
        driver.get(BASE_URL)
        html_content = driver.page_source

        # Find the <span> element with the specified text
        span_element = driver.find_element(By.XPATH, "//span[contains(text(), ' properties')]")

        # Get the text content of the found element and split it
        result_text = span_element.text
        result_parts = result_text.split()
        result_parts = result_parts[0].replace(",", "")
        # Calculate the number of pages based on the total results and items per page
        total_results = int(result_parts)
        N_PAGES = math.ceil(total_results / PER_PAGE)

        print(f'There are {N_PAGES} different pages')
        return N_PAGES

    except Exception as e:
        print("Error:", e)

    finally:
        driver.quit()


def get_link(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        html_content = driver.page_source
        time.sleep(3)
        soup = BeautifulSoup(html_content, 'html.parser')
        async_scripts = soup.find_all('script')
        pattern = r'Hotel_Review.*?\.html'
        results = []
        for script_tag in async_scripts:
            matches = re.findall(pattern, script_tag.text)
            if matches:
                results.extend(matches)
        return results
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    N_PAGES = get_number_of_pages(BASE_URL, PER_PAGE)
    counter = 0
    links = []
    for i in range(N_PAGES):
        print(counter)
        counter += 1
        url = get_listing_url(i)
        link = get_link(url)
        links.extend(link)

with open("links_rome.csv", mode='a+', newline='') as file:
    writer = csv.writer(file)  # Pass the 'file' object here
    for item in links:
        writer.writerow([item])