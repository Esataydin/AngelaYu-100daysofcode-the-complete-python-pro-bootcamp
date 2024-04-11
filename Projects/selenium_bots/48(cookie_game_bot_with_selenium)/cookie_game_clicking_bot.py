from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

# It crashes if it clicks over and over again
url = "http://orteil.dashnet.org/experiments/cookie/"

# chromedriver must be downloaded in your PC, you can download here: https://googlechromelabs.github.io/chrome-for-testing/#stable
ser = Service("C:\Development\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get(url)

# Gets cookie object to click on.
cookie = driver.find_element(By.ID, "cookie")

# Gets upgrade item ids.
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Gets all upgrade <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        # Converts <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Creates dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Gets current cookie count
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Finds upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                 affordable_upgrades[cost] = id

        # Purchases the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        driver.find_element(By.ID, to_purchase_id).click()
        
        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes it stops the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break

