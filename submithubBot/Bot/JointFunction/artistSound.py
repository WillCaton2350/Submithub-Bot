from States.data import similar_artists, save_artist_Btn, genre_Select,first_Curator, close_genre_Btn
from States.data import add_ArtistBtn, next_Xpath, add_Genre, next_Btn_Xpath,next_payment
from States.data import similar_Hiphop_Artist_list,artistSearch,genreType, url
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import NoSuchElementException
from States.data import geckoDriverPath, curatorDashboard
from States.data import moods_Opts, submit_toPlaylist
from urllib.error import HTTPError as PageNotFoundError
from selenium.webdriver.common.by import By 
from selenium import webdriver as web
from time import sleep  
import random
import os

class webDriverSound:
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

    def Sound_Alike(self):
            print("sound alike")
            try:
                WDW(
                    self.driver,10
                ).until(EC.presence_of_element_located((
                By.XPATH,similar_artists
                )))
            except NoSuchElementException as e:
                print(e)
            sleep(2)
            similar_artists_input = self.driver.find_element(
                By.XPATH,
                artistSearch
                )
            random.shuffle(similar_Hiphop_Artist_list)
            for artist in similar_Hiphop_Artist_list[:5]:
                similar_artists_input.send_keys(
                    artist)
                try:
                    WDW(
                        self.driver,10).until(
                    EC.presence_of_element_located((
                    By.XPATH,
                    add_ArtistBtn)))
                except ElementNotInteractableException as e:
                    print(e)
                self.driver.find_element(
                    By.XPATH,
                    add_ArtistBtn).click()
                print("add_ArtistBtn clicked")
                self.driver.find_element(
                    By.XPATH,
                    save_artist_Btn).click()
                print("save_ArtistBtn clicked")
                sleep(1)
                self.driver.find_element(
                    By.XPATH,add_Genre).click()
                print("add_Genre clicked")
                sleep(1)
                element = self.driver.find_element(
                    By.ID,
                    "search-genres")
                self.driver.execute_script(
                    "arguments[0].scrollIntoView();", 
                    element)
                element.send_keys(
                    genreType)
                print(genreType," - keys sent")
                sleep(1)
                self.driver.find_element(
                    By.XPATH,
                    genre_Select).click()
                print("genre selected clicked")
                sleep(1)
                self.driver.find_element(
                    By.CSS_SELECTOR,
                    close_genre_Btn
                    ).click()
                print("close genre btn clicked")
                sleep(1)
                self.driver.execute_script(
                "arguments[0].scrollIntoView();",
                self.driver.find_element(
                    By.XPATH,
                    moods_Opts
                    ))
                self.driver.find_element(
                    By.XPATH,
                    moods_Opts).click()
                print("moods clicked")
                sleep(1)
                try:
                    self.driver.find_element(
                        By.XPATH,
                        next_Xpath).click()
                    print("next btn clicked")
                except ElementNotInteractableException as err:
                    print(err)
                sleep(1)
                self.driver.find_element(
                    By.XPATH,
                next_Btn_Xpath).click()
                print("next btnXPATH clicked")
                sleep(2)
                print("payment Function")
                sleep(1)
                self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            self.driver.find_element(
                By.XPATH,
                curatorDashboard
                ))
                print("Scrolled to Element: found")
                sleep(2)
                self.driver.find_element(
                    By.XPATH,
                first_Curator).click()
                print("clicked","first_Curator")
                sleep(1)
                self.driver.find_element(
                    By.XPATH,
                submit_toPlaylist).click()
                print("clicked","submit_toPlaylist")
                self.driver.find_element(
                    By.XPATH,
                next_payment).click()
                print("clicked","next_payment")
                sleep(2)