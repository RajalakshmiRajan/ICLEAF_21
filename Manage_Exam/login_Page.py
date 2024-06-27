from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utils import WebPageUtils
import time
import configparser



config=configparser.RawConfigParser()
config.read('config.properties')

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def language_select(self):
        try:
            time.sleep(1)
            select_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "select"))
            )
            select = Select(select_element)
            select.select_by_value("french")
            time.sleep(1)
            select.select_by_value("english")
        except StaleElementReferenceException:
            self.language_select()

    def clear_password_field(self, password_element):
        password_element.click()
        ActionChains(self.driver).send_keys(Keys.BACKSPACE * 20).perform()

    def clear_username_field(self, username_element):
        username_element.click()
        ActionChains(self.driver).send_keys(Keys.BACKSPACE * 20).perform()

    def click_eye_icon(self):
        eye_icon = self.driver.find_element(By.CSS_SELECTOR,config.get('ME',   'eye_icon'))
        eye_icon.click()

    def login(self):
        try:
            username_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "username")))
            utils = WebPageUtils(self.driver)
            utils.url_display()
            password_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID,"password")))
            self.clear_username_field(username_field)
            time.sleep(1)
            self.clear_password_field(password_field)
            time.sleep(1)

            username_field.send_keys(config.get('ME', 'username'))
            password_field.send_keys(config.get('ME', 'password'))
            time.sleep(1)
            self.click_eye_icon()
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME',   'login_button'))))
            login_button.click()
            try:
                okay_button = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((By.CLASS_NAME,config.get('ME',    'okay_button'))))
                okay_button.click()
                print("Login failed. Invalid username or password.")
                time.sleep(3)
                return False
            except:
                print("Login successful!")
                return True
        except Exception as e:
            print(f"An error occurred during login: {e}")
            return False

