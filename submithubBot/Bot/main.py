from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import NoSuchElementException
from urllib.error import HTTPError as PageNotFoundError
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium import webdriver as web
from States.data import *
from time import sleep
import random   
import os

class webDriver:
    def __init__(self):
        self.driver = None
    def start_driver(self):
        print(print_var_start_driver)
        firefox_options = web.FirefoxOptions()
        os.environ[
            os_env
            ] =  gecko_driver_path
        self.driver = web.Firefox(
            options=firefox_options        
        )
        self.driver.maximize_window()
    def browser(self):
        print(print_var_browser)
        self.driver.get(url)
        try:
            WDW(
                self.driver, 
                timeout=10).until(
                    EC.url_matches(
                        url))
        except PageNotFoundError as err:
            if err.code == 404:
                print(err_pg)
        # add exceptions not just print statements
    def login(self):
        print(print_var_login)
        try:
            WDW(
                self.driver,
                timeout=10
                ).until(
            EC.presence_of_element_located((
            By.XPATH,login_btn
            )))
        except NoSuchElementException as err:
            print(err)
        self.driver.find_element(
            By.XPATH,login_btn).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(
            By.XPATH,
            username_field).send_keys(
        username)
        self.driver.find_element(
            By.XPATH,
            password_field).send_keys(
        password)
        self.driver.find_element(
            By.XPATH,
            login_submit_btn).send_keys(
                Keys.ENTER)
        sleep(3)
    def submit_song(self):
        print(print_var_submit_song)
        try:
            WDW(
                self.driver,
                timeout=20
                ).until(
            EC.presence_of_element_located((
            By.XPATH,submit_a_song_sidebar_btn
            )))
        except NoSuchElementException as err:
            print(err)
        self.driver.find_element(
            By.XPATH,
            submit_a_song_sidebar_btn).click()
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
            sound_cloud)
        
    def scroll_view(self):
        print(print_var_scroll_view)
        sleep(5)
        self.driver.implicitly_wait(5)
        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
        self.driver.find_element(
            By.CSS_SELECTOR, 
            song_released_text
            ))
        try:
            WDW(
                self.driver, 10).until(
            EC.presence_of_element_located((
            By.CSS_SELECTOR, song_released_text
            )))
            self.driver.find_element(
            By.XPATH,
            is_released).click()
            print(print_var_clicked_btn)
        except ElementClickInterceptedException as err:
            print(err)
        finally:
            sleep(2)
        self.driver.find_element(
            By.XPATH,release_date)
        self.driver.find_element(
            By.XPATH,
            release_date).send_keys(
                Keys.COMMAND + cmd_key)
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

    def artist_info(self):
        print(print_var_artist_info)
        try:
            WDW(
                self.driver,10).until(
            EC.presence_of_element_located((
            By.XPATH,artist_name_field)))
            self.driver.find_element(
                By.XPATH,
                artist_name_field
                ).send_keys(artist_name_text)
        except NoSuchElementException as err:
            print(err)
        sleep(2)
        self.driver.find_element(
            By.XPATH,
            new_artist).click()
        try:
            WDW(
                self.driver,
                10).until
            EC.presence_of_element_located(((
                By.XPATH,
                select_country)))
        except NoSuchElementException as e:
            print(e)
        self.driver.find_element(
            By.XPATH,select_country
            ).send_keys(
                US)
        try:
            WDW(
                self.driver,
                10).until
            EC.presence_of_element_located(((
                By.XPATH,
                featured_artists_btn)))
        except NoSuchElementException as err:
            print(err)
        self.driver.find_element(
            By.XPATH,
        featured_artists_btn).click()
        print(print_var_featured_artists_btn)
        try:
            self.driver.find_element(
                By.XPATH,
            featured_artist_name_field
            ).send_keys(feature_name)
            print(print_var_feature_name_keys,
                  feature_name)
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
            featured_artists_btn3
            ).click()
        print(print_var_featured_artists_btn3,
              featured_artists_btn3)
        sleep(2)
        self.driver.find_element(
            By.XPATH,select_country_2
            ).send_keys(
                US)
        sleep(2)
        try:
            WDW(
                self.driver,10).until(
            EC.presence_of_element_located((
            By.XPATH,song_title_field)))
            self.driver.find_element(
                By.XPATH,
                song_title_field).send_keys(
                    song_title)
            sleep(2)
        except NoSuchElementException as e:
            print(e)
        self.driver.find_element(
            By.XPATH,
            next_btn_).click()
        print(print_var_next_btn_)
        sleep(2)
        try:
            WDW(
                self.driver,10
            ).until(EC.presence_of_element_located((
            By.CSS_SELECTOR,main_artist_option)))
        except NoSuchElementException as e:
            print(e)
        self.driver.find_element(
            By.CSS_SELECTOR,
            main_artist_option).click()
        try:
            WDW(
                self.driver,10
            ).until(EC.presence_of_element_located((
            By.XPATH,lyrics_option
            )))
        except NoSuchElementException as e:
            print(e)
        self.driver.find_element(
            By.XPATH,
            lyrics_option).click()
        try:
            WDW(
                self.driver,10
            ).until(EC.presence_of_element_located((
            By.XPATH,lyrics_lang
            )))
        except NoSuchElementException as e:
            print(2)
        self.driver.find_element(
            By.XPATH,
            lyrics_lang).click()
        try:
            WDW(
                self.driver,10
            ).until(EC.presence_of_element_located((
            By.XPATH,explicit_lyrics
            )))
        except NoSuchElementException as e:
            print(e)
        self.driver.find_element(
            By.XPATH,
            explicit_lyrics).click()
        sleep(1)
        try:
            WDW(
                self.driver,10
            ).until(EC.presence_of_element_located((
            By.XPATH,no_clean_version
            )))
        except NoSuchElementException as e:
            print(e)
        self.driver.find_element(
            By.XPATH,
            no_clean_version).click()
        try:
            WDW(
                self.driver,10
            ).until(EC.presence_of_element_located((
            By.XPATH,insert_lyrics_text_area
            )))
        except NoSuchElementException as e:
            print(e)
        self.driver.find_element(
            By.XPATH,
            insert_lyrics_text_area).send_keys(lyrics_text)
        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
        self.driver.find_element(
            By.XPATH,
            finish_upload
            ))
        try:
            WDW(
                self.driver,10
            ).until(EC.presence_of_element_located((
            By.XPATH,finish_upload
            )))
            sleep(2)
        except NoSuchElementException as e:
            print(e)
        self.driver.find_element(
            By.XPATH,
            finish_upload).click()
        
    def playlist_submission(self):
        print(print_var_playlist_submission)
        try:
            WDW(
                self.driver,10
            ).until(EC.presence_of_element_located((
            By.XPATH,submit_to_curators
            )))
            sleep(2)
        except NoSuchElementException as e:
            print(e)
        self.driver.find_element(
            By.XPATH,
            submit_to_curators).click()
        print("clicked",submit_to_curators)
        try:
            WDW(
                self.driver,10
            ).until(EC.presence_of_element_located((
            By.XPATH,submit_to_curators_btn2
            )))
            self.driver.find_element(
                By.XPATH,
                submit_to_curators_btn2).click()
            print("clicked",submit_to_curators_btn2)
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
        
    def sound_a_like(self):
        print(print_var_sound_a_like)
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
            artist_search
            )
        random.shuffle(similar_hiphop_artist_list)
        for artist in similar_hiphop_artist_list[:5]:
            similar_artists_input.send_keys(
                artist)
            try:
                WDW(
                    self.driver,10).until(
                EC.presence_of_element_located((
                By.XPATH,
                add_artist_btn)))
            except ElementNotInteractableException as e:
                print(e)
            self.driver.find_element(
                By.XPATH,
                add_artist_btn).click()
            print(print_var_add_artist_btn)
            self.driver.find_element(
                By.XPATH,
                save_artist_btn).click()
            print(print_var_save_artist_btn)
            sleep(1)
            self.driver.find_element(
                By.XPATH,add_genre).click()
            print(print_var_add_genre)
            sleep(1)
            element = self.driver.find_element(
                By.ID,
                search_genre)
            self.driver.execute_script(
                "arguments[0].scrollIntoView();", 
                element)
            element.send_keys(
            # add a for loop for hip-hop sub genres 
            # possibly see if you can implement a 
            # list comprehension [for i in (container)]
                genre_type)
            print(genre_type," - keys sent")
            sleep(1)
            self.driver.find_element(
                By.XPATH,
                genre_select).click()
            print(print_var_genre_select)
            sleep(1)
            self.driver.find_element(
                By.CSS_SELECTOR,
                close_genre_btn
                ).click()
            print(print_var_close_genre_btn)
            sleep(1)
            self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            self.driver.find_element(
                By.XPATH,
                moods_opts
                ))
            self.driver.find_element(
                By.XPATH,
                moods_opts).click()
            print(print_var_moods_opts)
            sleep(1)
            try:
                self.driver.find_element(
                    By.XPATH,
                    next_xpath).click()
                print(print_var_next_xpath)
            except ElementNotInteractableException as err:
                print(err)
            sleep(1)
            self.driver.find_element(
                By.XPATH,
            next_btn_xpath).click()
            print(print_var_next_btn_xpath)
            sleep(2)
            print(print_var_payment_function)
            sleep(1)
            self.driver.execute_script(
        "arguments[0].scrollIntoView();",
        self.driver.find_element(
            By.XPATH,
            curator_dashboard))
            print(print_var_scrolled_to_element_curator_dashboard)
            sleep(2)
            self.driver.find_element(
                By.XPATH,
            first_curator).click()
            print(print_var_first_curator)
            sleep(1)
            self.driver.find_element(
                By.XPATH,
            submit_to_playlist).click()
            print(print_var_submit_to_playlist)
    def close_driver(self):
        self.driver.close()
        print(print_var_bot_closed)