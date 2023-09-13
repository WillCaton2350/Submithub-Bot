from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import NoSuchElementException
from urllib.error import HTTPError as PageNotFoundError
from States.data import submit_toCurators_btn2
from States.data import premium_credits, url
from selenium.webdriver.common.by import By 
from States.data import submit_toCurators
from States.data import geckoDriverPath
from selenium import webdriver as web
from time import sleep  
import os

class webDriverPList:
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


    def Playlist_submission(self):
            print("playlist submission")
            try:
                WDW(
                    self.driver,10
                ).until(EC.presence_of_element_located((
                By.XPATH,submit_toCurators
                )))
                sleep(2)
            except NoSuchElementException as e:
                print(e)
            self.driver.find_element(
                By.XPATH,
                submit_toCurators).click()
            print("clicked",submit_toCurators)
            try:
                WDW(
                    self.driver,10
                ).until(EC.presence_of_element_located((
                By.XPATH,submit_toCurators_btn2
                )))
                self.driver.find_element(
                    By.XPATH,
                    submit_toCurators_btn2).click()
                print("clicked",submit_toCurators_btn2)
                sleep(2)
            except NoSuchElementException as e:
                print(e)
            try:
                WDW(
                    self.driver,10
                ).until(EC.presence_of_element_located((
                By.XPATH,premium_credits
                )))
                sleep(2)
            except NoSuchElementException as e:
                print(e)
            self.driver.find_element(
                By.XPATH,
                premium_credits).click()
            print("clicked",premium_credits)