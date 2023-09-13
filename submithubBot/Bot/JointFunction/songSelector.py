from States.data import is_released, release_date, date, url,next_btn,songReleased_Text
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import NoSuchElementException
from urllib.error import HTTPError as PageNotFoundError
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from States.data import geckoDriverPath
from selenium import webdriver as web
from time import sleep  
import os

class webDriverSelect:
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


    def scrollView(self):
            print("scrollView")
            sleep(5)
            self.driver.implicitly_wait(5)
            self.driver.execute_script(
                "arguments[0].scrollIntoView();",
            self.driver.find_element(
                By.CSS_SELECTOR, 
                songReleased_Text
                ))
            try:
                WDW(
                    self.driver, 10).until(
                EC.presence_of_element_located((
                By.CSS_SELECTOR, songReleased_Text
                )))
                self.driver.find_element(
                By.XPATH,
                is_released).click()
                print("clickedBTN")
            except ElementClickInterceptedException as err:
                print(err)
            finally:
                sleep(2)
            self.driver.find_element(
                By.XPATH,release_date)
            self.driver.find_element(
                By.XPATH,
                release_date).send_keys(
                    Keys.COMMAND + 'a')
            self.driver.find_element(
                By.XPATH,
                release_date).send_keys(
                    Keys.DELETE)
            sleep(1)
            self.driver.implicitly_wait(1)
            self.driver.find_element(
                By.XPATH,
                release_date).send_keys(
                    date)
            sleep(1)
            try:
                WDW(
                    self.driver,10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    next_btn
                )))
            except NoSuchElementException as e:
                print(e)
            finally:
                self.driver.find_element(
                    By.XPATH,
                    next_btn
                ).click()
            sleep(2)