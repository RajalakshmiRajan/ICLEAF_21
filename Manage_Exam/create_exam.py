from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from utils import WebPageUtils
import time
import configparser
import mysql.connector
from db_utils import query_database


config=configparser.RawConfigParser()
config.read('config.properties')

class CreateExamPage:

    def __init__(self, driver):
        self.driver = driver
    def create_exam(self):
        values_list = []
        try:
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME,config.get('ME',   'manage_exam')))).click()
            utils = WebPageUtils(self.driver)
            utils.url_display()
            create_exam_link = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ME','create_exam_link_css'))))
            create_exam_link.click()
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, config.get('ME','exam_admin_select_css')))).click()
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, config.get('ME',   'text_xpath')))).click()
            input_element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,config.get('ME',   'create_exam_input_css'))))
            input_element.click()
            input_element.send_keys("Java_Exam700123")
            input_element = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, config.get('ME',   'description_textarea'))))
            input_element.click()
            time.sleep(5)
            input_element.send_keys("sample7001")
            time.sleep(10)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", input_element)
            time.sleep(10)
            input_element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located( (By.XPATH, config.get('ME',   'exam_name_xpath'))))
            input_element.click()
            input_element.send_keys("50")
            time.sleep(2)
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, config.get('ME',   'radio_button')))).click()
            time.sleep(2)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", input_element)
            checkbox = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, config.get('ME',   'checkbox_xpath'))))
            if not checkbox.is_selected():
                checkbox.click()
            self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
            time.sleep(2)
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,config.get('ME',   'submit_button_xpath')))).click()
            time.sleep(2)
            self.driver.save_screenshot("/home/adminroot/PycharmProjec/pythonProject/Screenshots/create1.png")
            element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,config.get('ME',   'add_button'))))
            utils.scroll(By.XPATH, config.get('ME',   'add_button'))
            element.click()
            time.sleep(3)
            print("Exam created successfully")
            # Call get_created_exam_info after creating the exam
            self.get_created_exam_info()
        except Exception as e:
            print(f"An error occurred: {e}")

    def instructions(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH,config.get('ME',   'instruction_textarea')))).send_keys(
                "sample text here")
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME',   'remove_button')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME',   'add_button')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH,config.get('ME',   'instruction_textarea')))).send_keys(
                "sample text here")
            time.sleep(3)
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME',   'action1_button')))).click()
            time.sleep(5)
            WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME',   'duration_input')))).send_keys("30")
            WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME',   'easy_input')))).send_keys("4")
            WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME',   'hard_input')))).send_keys("1")
            WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME',   'marks_input')))).send_keys("0")
            time.sleep(1)
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH,config.get('ME',   'action1_button')))).click()
            utils = WebPageUtils(self.driver)
            utils.scroll(By.XPATH, config.get('ME',   'save_button_xpath'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME',   'save_button_xpath')))).click()
            time.sleep(5)
            self.driver.save_screenshot(
                "/home/adminroot/PycharmProjec/pythonProject/Screenshots/create2.png")
            message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,config.get('ME',   'create_pop_meassage'))))
            message_text = message_element.text
            print("Text message displayed above okay_button:", message_text)
            okay_button = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, config.get('ME',   'okay_button'))))
            button_text = okay_button.text
            print("Text from okay_button:", button_text)
            self.driver.save_screenshot("/ home / adminroot / PycharmProjec / pythonProject / Screenshots/create3.png")
            okay_button.click()
            time.sleep(5)
            print("Instructions updated successfully")
        except Exception as e:
            print(f"An error occurred: {e}")
            #Database
    def get_created_exam_info(self):
        try:
            exam_name = "Advanced Exam_121"

            query = "SELECT * FROM m_exam WHERE exam_name = %s"
            result = query_database(query, (exam_name,))
            if result:
                print("Exam Information:")
                for row in result:
                    for idx, field in enumerate(row):
                        print(f"{idx + 1}. {field}")
            else:
                print("No Exam found with the provided name:", exam_name)
        except Exception as e:
            print(f"An error occurred while fetching exam information: {e}")


        #sample

