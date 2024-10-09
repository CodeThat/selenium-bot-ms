import pandas as pd
import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException
from bs4 import BeautifulSoup

# Define your proxy settings
proxy_host = "127.0.0.1"
proxy_port = 1080

# Create a Proxy object and set the proxy type and address
proxy = Proxy()
proxy.proxy_type = ProxyType.SOCKS5 # Or manual proxy type can be used.
proxy.proxy_url = f"{proxy_host}:{proxy_port}"

# Set the proxy capabilities for the WebDriver
capabilities = webdriver.DesiredCapabilities.EDGE
proxy.add_to_capabilities(capabilities)

# Create the WebDriver instance with the proxy capabilities
driver = webdriver.Edge(desired_capabilities=capabilities)
driver.get("https://www.msbar.org/lawyer-directory.aspx")
driver.implicitly_wait(5)
driver.maximize_window()


def grab_all_data(file):
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    data = []
    divs = soup.find_all("section", {"class": "LawyerInformation cf"})
    for div in divs:
        lawyer = [tag.text.strip() for tag in div.find_all("div", {"class": "DataHolder"})]
        data.append(lawyer)
    df = pd.DataFrame(data)
    df.to_csv(file, index=False, header=True)


def navigate_web():
    print("Preparing to parse:", driver.title)
    for page_num in range(1, 6):
        try:
            print(f"Navigating to page {page_num} results...")
            search_box = driver.find_element(By.XPATH, "//input[@id='searchbox']")
            search_box.click()
            search_box.clear()
            search_box.send_keys(f"MS&page={page_num}&s={(page_num - 1) * 2000}")
            search_button = driver.find_element(By.XPATH, "//button[@id='searchbutton']")
            search_button.click()
            print("Resolving DOM...")

            print(f"Grabbing data from page {page_num}...")
            grab_all_data("data.csv")

        except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException) as e:
            print(f"Exception thrown: {str(e)}")
            break


def tear_down():
    print("Done enumerating:", driver.title)
    print("Closing webdriver instance...")
    driver.quit()


# Call main functions to run
navigate_web()
tear_down()
