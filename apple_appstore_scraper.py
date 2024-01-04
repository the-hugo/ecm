import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class App:
    service = Service('path/to/chromedriver')
    driver = webdriver.Chrome(service=service)
    url = f'https://apps.apple.com/us/app/id'

    def __init__(self, id, name, x):
        self.x = x
        self.id = str(id)
        self.name = name
        with open("appstore_data.csv", "a+", encoding="utf-8", newline="",) as file:
            self.app_file = {"x": x, "id": id, "name": name}

    def start_driver(self):
        self.driver.get(self.url+self.id)

    def __get_soup(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        return soup

    def get_category(self):
        soup = self.__get_soup()
        category_dt = soup.find('dt', string='Category')
        category_dd = category_dt.find_next_sibling('dd')
        category_a = category_dd.find('a')
        category_name = category_a.text
        self.app_file["category"] = category_name.strip()

    def click_button(self):
        try:
            time.sleep(1)
            buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button.we-modal__show.link.section__nav__see-all-link')
            for button in buttons:
                if "Version History" in button.text:
                    self.__get_version_history(button)
                if "See Details" in button.text:
                    self.__get_privacy_data(button)
        except:
            time.sleep(20)
            self.click_button()

    def __get_version_history(self, button):
        button.click()
        time.sleep(1)
        soup = self.__get_soup()
        time_tags = soup.find_all('time')
        dates = [tag.text for tag in time_tags if len(tag.text) > 10]
        self.app_file["version_history"] = dates
        close = self.driver.find_elements(By.CLASS_NAME, "we-modal__close")
        close[0].click()

    def __get_privacy_data(self, button):
        button.click()
        time.sleep(1)
        soup = self.__get_soup()
        modal_content = soup.find('div', {'id': 'modal-container'})
        for section in modal_content.find_all('div', {'class': 'app-privacy__modal-section'}):
            section_title = section.find('h2')
            if section_title:
                section_title_text = section_title.get_text(strip=True)
                if section_title_text == 'Data Linked to You':
                    self.app_file["Linked"] = section.get_text(strip=True)
                elif section_title_text == 'Data Used to Track You':
                    self.app_file["Tracked"] = section.get_text(strip=True)
                elif section_title_text == 'Data Not Linked to You':
                    self.app_file["N/Linked"] = section.get_text(strip=True)

    def get_price(self):
        soup = self.__get_soup()
        price_dt = soup.find('dt', string='Price')
        price_dd = price_dt.find_next_sibling('dd')
        price_name = price_dd.text
        self.app_file["price"] = price_name

    def get_ratings(self):
        soup = self.__get_soup()
        try:
            rating_obj = soup.find('span', {"class": "we-customer-ratings__averages__display"})
            rating_avg = rating_obj.text
            self.app_file["rating_avg"] = rating_avg
            rating_count = soup.select_one('.we-rating-count').text
            rating = rating_count.split("•")[1].strip()
            self.app_file["rating_num"] = rating
        except AttributeError:
            pass

    def write_csv(self):
        with open("appstore_data.csv", 'a+', newline="", encoding="utf-8") as file:  # opening initial file
            columns = ["x", "name", "id", "category", "price", "version_history", "rating_avg", "rating_num", "Linked", "Tracked", "N/Linked"]
            csv_writer = csv.DictWriter(file, fieldnames=columns)  # preparing file to write rows
            csv_writer.writerow(self.app_file)  # writing rows to file


if __name__ == "__main__":
    counter = 1
    check = False
    with open("cleaned_app_idx.csv", "r", encoding="utf-8") as file:
        for line in file:
            try:
                reader = csv.reader([line])
                x, name, idx = next(reader)
                if x == "5293":
                    check = True
                if check:
                    app = App(idx, name, x)
                    app.start_driver()
                    print(x, " :", idx)
                    app.get_price()
                    app.get_ratings()
                    app.get_category()
                    app.click_button()
                    app.write_csv()
            except AttributeError:
                print(f"Error {counter}")
                counter += 1