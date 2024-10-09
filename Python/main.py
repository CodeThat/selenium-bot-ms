# -*- coding: utf-8 -*-
import fileinput

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

# from selenium.webdriver.support.ui import Select as select
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# import selenium.webdriver.chrome.webdriver
# from selenium.webdriver.support import expected_conditions as EC

# Use Chrome as a service:
# from webdriver_manager.chrome import ChromeDriverManager
# service = ChromeService(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

# page_source = driver.page_source
# soup = BeautifulSoup(page_source, "html.parser")

driver = webdriver.Edge()
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
driver.get("https://www.msbar.org/lawyer-directory.aspx")
driver.implicitly_wait(5)
driver.maximize_window()
#wait = WebDriverWait(driver, timeout=10, poll_frequency=1,
#                    ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])


# Grab all data from page 1-5
def grab_all_data():
    with open("data.csv", 'a') as f:
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        data = []
        div = soup.find('section', {'id': "LawyerSearchResults"})
        for div in soup.find_all("section", {"class": "LawyerInformation cf"}):
            lawyer = [tag.text.strip() for tag in div.find_all("div", {"class": "DataHolder"})]
            # Write to CSV with fileinput
            data.append(lawyer)
            f.write(str(lawyer))
            # Save to CSV with Pandas
            # df = pd.DataFrame(data)
            # df.to_csv("data_pandas.csv", index=False, header=True)


"""def grab_hrefs():
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    for tag in soup.find_all(href=re.compile("@")):
        with open("emails.csv", 'a') as f:
            f.write(tag.text + '\n')"""


def navigate_web():
    print("Preparing to parse: ", driver.title)
    while True:
        try:
            # Nav to page 1: 0-2000 results
            print("Navigating to page 1 results...")
            driver.find_element(By.XPATH, "//input[@id='radio5']").click()
            driver.find_element(By.XPATH, "//input[@id='searchbox']").click()
            driver.find_element(By.XPATH, "//input[@id='searchbox']").clear()
            driver.find_element(By.XPATH, "//input[@id='searchbox']").send_keys("MS")
            driver.find_element(By.XPATH, "//button[@id='searchbutton']").click()
            print("Resolving DOM...")
            # time.sleep(3)

            # Enumerate page 1 results
            print("Grabbing emails from page 1...")
            # grab_hrefs()
            print("Grabbing data from page 1...")
            grab_all_data()

            # Nav to page 2: 2000-4000 results
            driver.find_element(By.XPATH, "//input[@id='searchbox']").click()
            driver.find_element(By.XPATH, "//input[@id='searchbox']").clear()
            driver.find_element(By.XPATH, "//input[@id='searchbox']").send_keys("MS&page=2&s=2000")
            driver.find_element(By.XPATH, "//button[@id='searchbutton']").click()
            print("Navigating to page 2...")
            print("Resolving DOM...")
            # time.sleep(3)

            # Enumerate page 2 results
            print("Grabbing emails from page 2...")
            # grab_hrefs()
            print("Grabbing data from page 2...")
            grab_all_data()

            # Nav to page 3: 4000-6000 results
            driver.find_element(By.XPATH, "//input[@id='searchbox']").clear()
            driver.find_element(By.XPATH, "//input[@id='searchbox']").click()
            driver.find_element(By.XPATH, "//input[@id='searchbox']").send_keys("MS&page=3&s=4000")
            driver.find_element(By.XPATH, "//button[@id='searchbutton']").click()
            print("Navigating to page 3...")
            # time.sleep(3)

            # Enumerate page 3 results
            print("Grabbing emails from 3...")
            # grab_hrefs()
            print("Grabbing data from 3...")
            grab_all_data()

            # Nav to page 4: 6000-8000 results
            driver.find_element(By.XPATH, "//input[@id='searchbox']").clear()
            driver.find_element(By.XPATH, "//input[@id='searchbox']").click()
            driver.find_element(By.XPATH, "//input[@id='searchbox']").send_keys("MS&page=4&s=6000")
            driver.find_element(By.XPATH, "//button[@id='searchbutton']").click()
            print("Navigating to next page 4...")
            # time.sleep(3)

            # Enumerate page 4 results
            print("Grabbing emails from page 4...")
            # grab_hrefs()
            print("Grabbing data from page 4...")
            grab_all_data()

            time.sleep(3)
            # Nav to page 5: 8000-10000 results
            driver.find_element(By.XPATH, "//input[@id='searchbox']").clear()
            driver.find_element(By.XPATH, "//input[@id='searchbox']").click()
            driver.find_element(By.XPATH, "//input[@id='searchbox']").send_keys("MS&page=5&s=8000")
            driver.find_element(By.XPATH, "//button[@id='searchbutton']").click()
            print("Navigating to next page 5...")
            # time.sleep(3)

            # Enumerate page 5 results
            print("Grabbing emails from page 5...")
            # grab_hrefs()
            print("Grabbing data from page 5...")
            grab_all_data()

        except NoSuchElementException:
            print("No such element found exception thrown")
        except ElementNotVisibleException:
            print("Element not visible exception thrown")
        except ElementNotSelectableException:
            print("Element not selectable exception thrown")
            break
        finally:
            break


# Close webdriver instance
def tear_down():
    print("Done enumerating: ", driver.title)
    print("Closing webdriver instance...")
    driver.close()


# Call main functions to run
navigate_web()
tear_down()

