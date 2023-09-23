from States.data import geckoDriverPath, loginBtn, usernameField
from States.data import passwordField, login_SubmitBtn, url
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import NoSuchElementException
from urllib.error import HTTPError as PageNotFoundError
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium import webdriver as web
from time import sleep  
import os


class webDriverLogin:
    def __init__(self):
        self.driver = None 
    def startDriver(self):
        print("start Driver")
        #self.driver = web.Safari()
        firefox_options = web.FirefoxOptions()
        os.environ[
            "webdriver.firefox.driver"
            ] =  geckoDriverPath
        self.driver = web.Firefox(
            options=firefox_options        
        )
        self.driver.maximize_window()
    def Browser(self):
        print("Browser")
        self.driver.get(url)
        try:
            WDW(
                self.driver, 
                timeout=10).until(
                    EC.url_matches(
                        url))
        except PageNotFoundError as err:
            if err.code == 404:
                print(
        "Error: Page not found")

    def login(self):
            print("Login")
            try:
                WDW(self.driver,timeout=10).until(EC.presence_of_element_located((By.XPATH,loginBtn)))
            except NoSuchElementException as err:
                print(err)
            self.driver.find_element(By.XPATH,loginBtn).click()
            self.driver.implicitly_wait(5)
            self.driver.find_element(
                By.XPATH,
                usernameField).send_keys(
            "username")
            self.driver.find_element(
                By.XPATH,
                passwordField).send_keys(
            "password")
            self.driver.find_element(
                By.XPATH,
                login_SubmitBtn).send_keys(
                    Keys.ENTER)
            sleep(3)
