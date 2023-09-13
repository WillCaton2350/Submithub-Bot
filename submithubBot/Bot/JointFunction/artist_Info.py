from States.data import geckoDriverPath, artistNameField,song_title_Field, newArtist
from States.data import no_clean_Version, insert_Lyrics_textArea, artistName
from States.data import select_Country, US,featuredArtistsBtn,mainArtistOption
from States.data import featuredArtistsBtn3, explicit_Lyrics, finish_Upload, url
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as WDW
from States.data import song_title, lyrics_Lang, lyrics_Text
from States.data import nextBtn,select_Country2, lyrics_Option
from selenium.common.exceptions import NoSuchElementException
from urllib.error import HTTPError as PageNotFoundError
from States.data import featureName, small_grey_text
from States.data import featuredArtistNameField
from selenium.webdriver.common.by import By 
from selenium import webdriver as web
from time import sleep  
import os


class webDriverArtist:
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

    def artistInfo(self):
            print("artistInfo")
            try:
                WDW(
                    self.driver,10).until(
                EC.presence_of_element_located((
                By.XPATH,artistNameField)))
                self.driver.find_element(
                    By.XPATH,
                    artistNameField
                    ).send_keys(artistName)
            except NoSuchElementException as err:
                print(err)
            sleep(2)
            self.driver.find_element(
                By.XPATH,
                newArtist).click()
            try:
                WDW(
                    self.driver,
                    10).until
                EC.presence_of_element_located(((
                    By.XPATH,
                    select_Country)))
            except NoSuchElementException as e:
                print(e)
            self.driver.find_element(
                By.XPATH,select_Country
                ).send_keys(
                    US)
            try:
                WDW(
                    self.driver,
                    10).until
                EC.presence_of_element_located(((
                    By.XPATH,
                    featuredArtistsBtn)))
            except NoSuchElementException as err:
                print(err)
            self.driver.find_element(
                By.XPATH,
            featuredArtistsBtn).click()
            print("featuredArtistsBtn clicked")
            try:
                self.driver.find_element(
                    By.XPATH,
                featuredArtistNameField
                ).send_keys(featureName)
                print("featuredName - keys sent",featureName)
            except NoSuchElementException as e:
                print(e)
            self.driver.execute_script(
                "arguments[0].scrollIntoView();",
            self.driver.find_element(
                By.XPATH, 
                small_grey_text
                ))
            sleep(1)
            self.driver.find_element(
                By.XPATH,
                featuredArtistsBtn3
                ).click()
            print("featuredArtistsBtn3 clicked",featuredArtistsBtn3)
            sleep(2)
            self.driver.find_element(
                By.XPATH,select_Country2
                ).send_keys(
                    US)
            sleep(2)
            try:
                WDW(
                    self.driver,10).until(
                EC.presence_of_element_located((
                By.XPATH,song_title_Field)))
                self.driver.find_element(
                    By.XPATH,
                    song_title_Field).send_keys(
                        song_title)
                sleep(2)
            except NoSuchElementException as e:
                print(e)
            self.driver.find_element(
                By.XPATH,
                nextBtn).click()
            print("Btn Clicked")
            sleep(2)
            try:
                WDW(
                    self.driver,10
                ).until(EC.presence_of_element_located((
                By.CSS_SELECTOR,mainArtistOption)))
            except NoSuchElementException as e:
                print(e)
            self.driver.find_element(
                By.CSS_SELECTOR,
                mainArtistOption).click()
            try:
                WDW(
                    self.driver,10
                ).until(EC.presence_of_element_located((
                By.XPATH,lyrics_Option
                )))
            except NoSuchElementException as e:
                print(e)
            self.driver.find_element(
                By.XPATH,
                lyrics_Option).click()
            try:
                WDW(
                    self.driver,10
                ).until(EC.presence_of_element_located((
                By.XPATH,lyrics_Lang
                )))
            except NoSuchElementException as e:
                print(2)
            self.driver.find_element(
                By.XPATH,
                lyrics_Lang).click()
            try:
                WDW(
                    self.driver,10
                ).until(EC.presence_of_element_located((
                By.XPATH,explicit_Lyrics
                )))
            except NoSuchElementException as e:
                print(e)
            self.driver.find_element(
                By.XPATH,
                explicit_Lyrics).click()
            sleep(1)
            try:
                WDW(
                    self.driver,10
                ).until(EC.presence_of_element_located((
                By.XPATH,no_clean_Version
                )))
            except NoSuchElementException as e:
                print(e)
            self.driver.find_element(
                By.XPATH,
                no_clean_Version).click()
            try:
                WDW(
                    self.driver,10
                ).until(EC.presence_of_element_located((
                By.XPATH,insert_Lyrics_textArea
                )))
            except NoSuchElementException as e:
                print(e)
            self.driver.find_element(
                By.XPATH,
                insert_Lyrics_textArea).send_keys(lyrics_Text)
            self.driver.execute_script(
                "arguments[0].scrollIntoView();",
            self.driver.find_element(
                By.XPATH, 
                finish_Upload
                ))
            try:
                WDW(
                    self.driver,10
                ).until(EC.presence_of_element_located((
                By.XPATH,finish_Upload
                )))
                sleep(2)
            except NoSuchElementException as e:
                print(e)
            self.driver.find_element(
                By.XPATH,
                finish_Upload).click()