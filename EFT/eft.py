from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time



column_values = []

# Read the CSV file and store the specified column in the list
with open("AssetNamesApes.csv", 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Append the value from the specified column to the list
        column_values.append(row["0"])

def get_data(id, retries=3):
    if retries == 0:
        print("Max retries reached. Exiting.")
        return

    hits = []
    print(f"\nStarting... with ID {id}")
    counter = 0
    found = False

    while len(hits) < 1:
        if counter > 0:
            hits = []
        if found:
            print("Moving on")
            return

        counter += 1
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
        base_url = "https://opensea.io/de-DE/assets/ethereum/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/"
        driver = webdriver.Chrome(options=options)
        time.sleep(3)
        driver.get(base_url + id)
        print("# of Trials:", counter)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='row']"))
            )
            buttons = driver.find_elements(By.XPATH, "//div[@role='row']")
            for div in buttons:
                divs = div.find_elements(By.TAG_NAME, "div")
                for el in divs:
                    try:
                        span = el.find_element(By.TAG_NAME, "span")
                        found = True
                        if span.text == "Verkauf":
                            hits.append(div)
                    except:
                        continue

        except Exception as e:
            driver.quit()
            print("Failed to locate Element")
            # Recursive call with decreased number of retries
            get_data(id, retries=retries - 1)
            return

    print(f"Found {len(hits)} elements")

    try:
        for row in hits:
            hover = row.find_elements(By.CSS_SELECTOR, 'div[data-testid="EventTimestamp"]')
            if len(hover) > 0:
                try:
                    action = ActionChains(driver)
                    action.move_to_element(hover[0]).perform()
                    driver.implicitly_wait(5)
                    html = driver.page_source
                    soup = BeautifulSoup(html, "html.parser")
                    div = soup.find("div", class_="tippy-content")
                    content = div.find_next("span").text
                    print(content)
                    temp_d = {
                        "id": id,
                        "content": content
                    }
                    with open("buy_history.csv", mode='a+', newline='', encoding='utf-8') as csv_file:
                        fieldnames = ['id', 'content']
                        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        writer.writerow(temp_d)
                except Exception as e:
                    print("Failed")
                    pass
    except Exception as e:
        print("Error processing elements")

    driver.quit()


for i in column_values:
    get_data(i)