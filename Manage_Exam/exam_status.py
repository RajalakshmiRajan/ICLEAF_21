from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from utils import WebPageUtils
import configparser


config=configparser.RawConfigParser()
config.read('config.properties')
class ExamStatusPage:
    def __init__(self, driver):
        self.driver = driver

    def exam_status(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CLASS_NAME, config.get('ME',   'manage_exam')))).click()
            time.sleep(2)
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,config.get('ME',   'exam_status_view')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,config.get('ME',   'exam_name')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH,config.get('ME',   'subject')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH,config.get('ME',   'subject_drop_down')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH,config.get('ME',   'exam')))).click()
            time.sleep(2)
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH,config.get('ME',   'search_specific_exam')))).send_keys("67511")
            time.sleep(5)
            self.driver.save_screenshot(
                "/home/adminroot/PycharmProjec/pythonProject/Screenshots/status1.png")
            message_found = False
            for i in range(2):
                WebDriverWait(self.driver, 30).until(
                    EC.invisibility_of_element_located((By.CSS_SELECTOR,config.get('ME',   'select'))))
                WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR,config.get('ME',   'view_button')))).click()
                time.sleep(2)
                try:
                    message_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((
                        By.XPATH,config.get('ME',   'message_test'))))
                    message_text = message_element.text
                    print("Text message displayed above okay_button:", message_text)
                    if "Exam Re-assigned Successfully!" in message_text or "Exam stopped successfully!" in message_text:
                        message_found = True
                        break
                except Exception:
                    continue
            if message_found:
                okay_button = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((By.CLASS_NAME,config.get('ME',   'okay_button'))))
                okay_button.click()
            else:
                print("Error message")
            self.driver.save_screenshot(
                "/home/adminroot/PycharmProjec/pythonProject/Screenshots/Status2.png")
            time.sleep(2)
            print("Exam status checked successfully")
        except Exception as e:
            print(f"An error occurred: {e}")


