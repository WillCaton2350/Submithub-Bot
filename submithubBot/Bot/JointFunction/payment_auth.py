from States.data import geckoDriverPath,cardNumInput,expDate,cardNum,zipCode,zipCodeInput
from States.data import cvv_Input,CVV, url, confirmPaymentBtn,exp_Date_Input
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as WDW
from urllib.error import HTTPError as PageNotFoundError
from selenium.webdriver.common.by import By 
from selenium import webdriver as web
from time import sleep  
import os




class webDriverPayment:
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
    def paymentAuth(self):
        # LOCATE PAYMENT BUTTON ON POP UP FORM
        #######################################
        try:
            WDW(
                self.driver, 10).until(
            EC.presence_of_element_located((
            By.XPATH,
            confirmPaymentBtn
            )))
            print("confirm payment btn: found")
        except ElementNotInteractableException as err:
            print(err)
        sleep(3)
        # PAYMENT CARD DETAILS
        ########################################
        try:
            cardNumElement = self.driver.find_element(
                By.CSS_SELECTOR, cardNumInput)
            actions = AC(self.driver)
            actions.move_to_element(
                cardNumElement).perform()
            sleep(0.5)
            self.driver.find_element(
                By.CSS_SELECTOR,
                cardNumInput).send_keys(
                    cardNum)
            print("written √")
        except StaleElementReferenceException as err:
            print(err)
        sleep(1)
        self.driver.find_element(
            By.XPATH,
            cvv_Input).send_keys(
                CVV)
        print("written √")
        sleep(1)
        self.driver.find_element(
            By.XPATH,
            exp_Date_Input).send_keys(
                expDate)
        print("written √")
        sleep(1)
        self.driver.find_element(
            By.XPATH,
            zipCodeInput).send_keys(
                zipCode)
        print("written √")
        try:
            WDW(
                self.driver, 10).until(
            EC.presence_of_element_located((
            By.XPATH,
            confirmPaymentBtn
            )))
            print("confirm payment btn: found")
        except ElementNotInteractableException as err:
            print(err)
        sleep(2)
        self.driver.find_element(
            By.XPATH,
            confirmPaymentBtn).click()
        print("confirm payment btn: clicked")