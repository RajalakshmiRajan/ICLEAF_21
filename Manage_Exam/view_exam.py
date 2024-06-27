from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from utils import WebPageUtils
import configparser



config=configparser.RawConfigParser()
config.read('config.properties')

class ViewExamPage:
    def __init__(self, driver):
        self.driver = driver

    def exam_view(self):
        try:
            # Navigate to the view exam page
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CLASS_NAME, config.get('ME',  'manage_exam')))).click()
            time.sleep(2)
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ME',  'view_exam')))).click()

            # Select the exam category
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,config.get('ME',  'exam_name')))).click()
            time.sleep(1)
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME', 'subject')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH,  config.get('ME', 'search_button')))).click()

            # Search for the specific exam
            time.sleep(1)
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'search_specific_exam')))).send_keys(
                "Advanced Exam1")
            time.sleep(5)

            # Click the edit button to view exam details
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ME', 'view_button')))).click()
            time.sleep(3)

            # Take screenshots of the exam details
            self.driver.save_screenshot("/home/adminroot/PycharmProjec/pythonProject/Screenshots/view1.png")
            ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(1)
            ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(3)
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'search_exam')))).send_keys(
                "Intro")
            time.sleep(3)
            self.driver.save_screenshot("/home/adminroot/PycharmProjec/pythonProject/Screenshots/view3.png")
            print("View the status of Exam details successfully")
        except Exception as e:
            print(f"An error occurred: {e}")
