from States.data import geckoDriverPath, loginBtn, usernameField, song_link,artistNameField,song_title_Field, newArtist, curatorDashboard,zipCodeInput
from States.data import no_clean_Version, insert_Lyrics_textArea, submit_toCurators_btn2, artistName, moods_Opts, submit_toPlaylist,cardNum,zipCode
from States.data import submitASong_sidebar_Btn,similar_artists, save_artist_Btn, featureName, genre_Select,first_Curator,expDate, small_grey_text
from States.data import select_Country, US, songReleased_Text, featuredArtistsBtn,mainArtistOption, close_genre_Btn,next_payment, cardNumInput
from States.data import passwordField, login_SubmitBtn, next_btn, song_title, lyrics_Lang, lyrics_Text, submit_toCurators,exp_Date_Input
from States.data import nextBtn,select_Country2, lyrics_Option, add_ArtistBtn, next_Xpath, add_Genre, next_Btn_Xpath,confirmPaymentBtn
from States.data import soundcloud,featuredArtistNameField, is_released, release_date, date,similar_Hiphop_Artist_list,artistSearch
from States.data import featuredArtistsBtn3, explicit_Lyrics, finish_Upload, premium_credits, cvv_Input,CVV,genreType, url
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import NoSuchElementException
from urllib.error import HTTPError as PageNotFoundError
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium import webdriver as web
from time import sleep  
import random   
import os

class webDriver:
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
            WDW(
                self.driver,
                timeout=10
                ).until(
            EC.presence_of_element_located((
            By.XPATH,loginBtn
            )))
        except NoSuchElementException as err:
            print(err)
        self.driver.find_element(
            By.XPATH,loginBtn).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(
            By.XPATH,
            usernameField).send_keys(
        "email@gmailcom")
        self.driver.find_element(
            By.XPATH,
            passwordField).send_keys(
        "password1234")
        self.driver.find_element(
            By.XPATH,
            login_SubmitBtn).send_keys(
                Keys.ENTER)
        sleep(3)

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
            #self.driver.find_element(
            #    By.XPATH,
            #next_payment).click()
            #print("clicked","next_payment")
            sleep(2)
    def close(self):
        print("Bot Closed")
        self.driver.close()
