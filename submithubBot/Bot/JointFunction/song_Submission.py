from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import NoSuchElementException
from urllib.error import HTTPError as PageNotFoundError
from States.data import geckoDriverPath, song_link
from States.data import submitASong_sidebar_Btn
from selenium.webdriver.common.by import By 
from States.data import soundcloud, url
from selenium import webdriver as web
import os

class webDriverSub:
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


    def submitSong(self):
            print("submitSong")
            try:
                WDW(
                    self.driver,
                    timeout=20
                    ).until(
                EC.presence_of_element_located((
                By.XPATH,submitASong_sidebar_Btn
                )))
            except NoSuchElementException as err:
                print(err)
            self.driver.find_element(
                By.XPATH,
                submitASong_sidebar_Btn).click()
            try:
                WDW(
                    self.driver,
                    timeout=20
                    ).until(
                EC.presence_of_element_located((
                By.XPATH,song_link
                )))
            except NoSuchElementException as err:
                print(err)
            finally:
                pass
            songLink = self.driver.find_element(
                By.XPATH,
                song_link)
            songLink.send_keys(
                soundcloud)