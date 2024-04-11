from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import time


URL = "https://www.speedtest.net"
URL_TWITTER = "https://twitter.com"
twitter_username = YOUR_TWITTER_USERNAME
twitter_password = YOUR_TWITTER_PASSWORD
delay = 6


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = None
        self.up = None
        # chromedriver must be downloaded in your PC, you can download here: https://googlechromelabs.github.io/chrome-for-testing/#stable
        ser = Service("C:\Development\chromedriver.exe")
        op = webdriver.ChromeOptions()
        self.s = webdriver.Chrome(service=ser, options=op)
        self.get_internet_speed()
        self.tweet_at_provider()

    def get_internet_speed(self) -> None:
        """Gets internet speed by testing it with bot made with Selenium"""
        self.s.maximize_window()
        self.s.get(URL)
        go_button = self.s.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(60)
        self.down = self.s.find_element(By.CSS_SELECTOR, '.download-speed').text
        self.up = self.s.find_element(By.CSS_SELECTOR, '.upload-speed').text

    def tweet_at_provider(self) -> None:
        """Tweets internet speed got by get_internet_speed() with bot made with Selenium"""
        self.s.maximize_window()
        self.s.get(URL_TWITTER)
        time.sleep(delay*2)
        login_button = self.s.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
        login_button.click()
        time.sleep(delay)
        login_input = self.s.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        login_input.send_keys(twitter_username)
        time.sleep(2)
        next_button = self.s.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_button.click()
        time.sleep(delay)
        password_input = self.s.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(twitter_password)
        time.sleep(2)
        login_button = self.s.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        login_button.click()
        time.sleep(delay*2)
        tweet_blank = self.s.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_blank.click()
        time.sleep(2)
        ActionChains(self.s).send_keys(f"Download:{self.down}  Upload:{self.up}").perform()
        time.sleep(2)
        tweeting_button = self.s.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
        tweeting_button.click()
        time.sleep(10)


bot = InternetSpeedTwitterBot()

