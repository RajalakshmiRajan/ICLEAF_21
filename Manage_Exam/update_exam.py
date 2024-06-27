from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils import WebPageUtils
import configparser



config=configparser.RawConfigParser()
config.read('config.properties')

class UpdateExamPage:
    def __init__(self, driver):
        self.driver = driver

    def exam_update(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CLASS_NAME, config.get('ME',  'manage_exam')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ME',  'update_exam')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,config.get('ME',   'list_exam')))).click()
            time.sleep(1)
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME',  'subject' )))).click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME',  'search_button')))).click()
            time.sleep(1)
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH,config.get('ME',   'search_specific_exam')))).send_keys("Advanced Exam1")
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME',   'edit_button')))).click()
            time.sleep(5)
            input_element = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH,config.get('ME', 'create_exam_input'))))
            input_element.click()
            input_element.send_keys("Advanced Exam123")

            input_element = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'description_textarea'))))
            input_element.click()
            time.sleep(5)
            input_element.send_keys("Advanced Exam1111030")
            time.sleep(10)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", input_element)
            time.sleep(10)

            input_element = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'exam_name_xpath'))))
            input_element.click()
            input_element.clear()
            input_element.send_keys("100")
            time.sleep(2)

            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH,config.get('ME',  'radio_button')))).click()
            time.sleep(2)

            checkbox = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH,config.get('ME',   'checkbox_xpath'))))
            if not checkbox.is_selected():
                checkbox.click()

            self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
            time.sleep(2)

            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME', 'add_button')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH,config.get('ME',    'instruction_textarea')))).send_keys("sample text here")
            time.sleep(1)
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME',  'action_button')))).click()
            time.sleep(3)

            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME',  'duration_input')))).send_keys("30")
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME',  'easy_input')))).send_keys("4")
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME',  'hard_input')))).send_keys("1")
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME',  'marks_input')))).send_keys("0")
            time.sleep(1)

            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME',  'action_button')))).click()
            self.driver.save_screenshot("/home/adminroot/PycharmProjec/pythonProject/Screenshots/update1.png")
            utils = WebPageUtils(self.driver)
            utils.scroll(By.XPATH, config.get('ME',  'update_button'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME',  'update_button')))).click()
            time.sleep(1)

            self.driver.save_screenshot("/home/adminroot/PycharmProjec/pythonProject/Screenshots/update2.png")
            time.sleep(3)

            button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[contains(@class, 'modalcommad_btn') and contains(@class, 'info')]"))
            )

            # Access the text child element within the button
            text_element = button.find_element(By.TAG_NAME, 'text')

            # Get the text content of the child element
            text_content = text_element.text
            print(text_content)

            # Click the button
            button.click()
            print("Exam updated successfully")
        except Exception as e:
            print(f"An error occurred: {e}")
