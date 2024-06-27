from cachetools import keys
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

class CreateCorporateCourse:

    def __init__(self, driver):
        self.driver = driver
    def create_corporate_course(self):

        try:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME', 'manage_corporate')))).click()
            time.sleep(2)
            utils = WebPageUtils(self.driver)
            utils.url_display()
            Manage_corp_c = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ME', 'manage_corporate_course'))))
            Manage_corp_c.click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME', 'create_corp_course_button')))).click()
            time.sleep(10)
            element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH,config.get('ME',  'course_type'))))
            ActionChains(self.driver).move_to_element(element).click().perform()

            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME', 'coursetype')))).click()

            input_element = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'subject_type'))))
            input_element.click()

            self.driver.execute_script("arguments[0].scrollIntoView(true);", input_element)
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME', 'subject_name')))).click()

            time.sleep(1)
            input_element = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'coursename'))))
            input_element.click()
            input_element.send_keys("Basic_Info")
            input_element = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'coursedesc'))))
            input_element.click()
            time.sleep(1)
            input_element.send_keys("Descrip")
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'courseprice')))).send_keys("500")
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'course_duration')))).send_keys("30")
            input_element = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'script_lan'))))
            input_element.click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME', 'script_subject')))).click()


            utils.scroll(By.XPATH, config.get('ME', 'save_button'))
            checkbox_xpaths = [
                config.get('ME', 'survey'),
                config.get('ME', 'certificate'),
                config.get('ME', 'exam_pack'),
                config.get('ME', 'course_progress'),
                config.get('ME', 'user_progress'),
                config.get('ME', 'course_track'),
                config.get('ME', 'navigate_section')
            ]

            # Loop through each checkbox XPATH
            for checkbox_xpath in checkbox_xpaths:
                checkbox = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, checkbox_xpath)))
                if not checkbox.is_selected():
                    checkbox.click()
                time.sleep(2)
                '''
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'certificate_no')))).send_keys("1")'''
            time.sleep(1)
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'mail_id')))).send_keys("admin@gmain.com")

            self.driver.save_screenshot("/home/adminroot/Python_Workspace/ICLEAF_21/screenshots/create_CorpCourse1.png")
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME', 'save_button')))).click()
            time.sleep(1)
            # Wait for the specific div to be visible
            parent_div = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'message2_f'))))

            # Find the span element inside the parent div
            message_element = parent_div.find_element(By.XPATH, config.get('ME', 'message2_c'))

            # Extract the text content from the span element
            message_text = message_element.text

            print("Pop-up Message:", message_text)

            print("Corporate course created successfully")
        except Exception as e:
            print(f"An error occurred: {e}")

    def edit_corp_course(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME', 'manage_corporate')))).click()
            time.sleep(2)
            utils = WebPageUtils(self.driver)
            utils.url_display()
            Manage_corp_c = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ME', 'manage_corporate_course'))))
            Manage_corp_c.click()
            time.sleep(3)
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'search_specific_exam')))).send_keys(
                "Test Automation")
            time.sleep(3)

            Manage_corp_c = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ME', 'edit_corp'))))
            Manage_corp_c.click()
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'edit')))).click()
            time.sleep(3)

            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'course_duration')))).send_keys("50")
            # Click on the SVG element
            input_element=WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ME', 'script_lan'))))
            input_element.click()
            time.sleep(2)
            input_element.send_keys("NA")
            time.sleep(2)
            ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME', 'button_syn')))).click()
            time.sleep(2)

            # Wait for the specific div to be visible
            parent_div = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, config.get('ME', 'message_f')))
            )

            # Find the span element inside the parent div
            message_element = parent_div.find_element(By.CSS_SELECTOR,config.get('ME', 'message_c'))

            # Extract the text content from the span element
            message_text = message_element.text

            print("Pop-up Message:", message_text)
            okay_button = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, config.get('ME', 'okay_button'))))
            self.driver.save_screenshot("/home/adminroot/Python_Workspace/ICLEAF_21/screenshots/create_CorpCourse2.png")
            okay_button.click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ME', 'save_button')))).click()


            # Wait for the specific div to be visible
            parent_div = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH,config.get('ME', 'message2_f'))))

            # Find the span element inside the parent div
            message_element = parent_div.find_element(By.XPATH,config.get('ME', 'message2_c'))

            # Extract the text content from the span element
            message_text = message_element.text

            print("Pop-up Message:", message_text)

            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, config.get('ME', 'okay1')))).click()



        except Exception as e:
            print(f"An error occurred: {e}")



    def manage_user(self):

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ME', 'manage_corporate')))).click()
        time.sleep(2)
        utils = WebPageUtils(self.driver)
        utils.url_display()
        Manage_corp_c = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ME', 'manage_corporate_course'))))
        Manage_corp_c.click()
        time.sleep(3)
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, config.get('ME', 'search_specific_exam')))).send_keys(
            "Test Automation")
        time.sleep(3)

        Manage_corp_c = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ME', 'edit_corp'))))
        Manage_corp_c.click()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, config.get('ME', 'manage_user')))).click()
        time.sleep(3)

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ME', 'assign_user')))).click()
        user=WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ME', 'search_user'))))

        user.click()

        user.send_keys("Ragu123")


        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, config.get('ME', 'user1_css')))).click()

        self.driver.save_screenshot("/home/adminroot/Python_Workspace/ICLEAF_21/screenshots/create_CorpCourse3.png")
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ME', 'Assign_bt')))).click()
        time.sleep(1)
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ME', 'close_bt')))).click()




    def track_user(self):


        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ME', 'track_user')))).click()
        user=WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ME', 'search_user'))))

        user.click()
        user.send_keys(Keys.CONTROL + 'a')
        user.send_keys(Keys.BACK_SPACE)
        user.send_keys("Nikitha")

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ME', 'daywise_rpt')))).click()

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ME', 'view_det')))).click()

        new_tab_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab_handle)
        ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, config.get('ME', 'close_icon')))).click()
        self.driver.save_screenshot("/home/adminroot/Python_Workspace/ICLEAF_21/screenshots/create_CorpCourse4.png")
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, config.get('ME', 'Yes_bt')))).click()

        try:
             # don't touch this line if u remove the code won't handle the Preview
            self.driver.switch_to.window(self.driver.window_handles[0])
        except Exception as e:
            pass

        time.sleep(1)
    def manage_batch(self):

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ME', 'manage_batch1')))).click()
        user=WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, config.get('ME', 'create_bt')))).click()

        batchname_input = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, 'batchname')))
        batchname_input.click()
        batchname_input.send_keys("Batch1")
        '''
        dropdown = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ME', 'drop_dn'))))
        dropdown.click()

        '''
        level_1= WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, config.get('ME', 'level1'))
        ))
        level_1.click()
        level_1.send_keys("ragu@yopmail.com")

        level_2 = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, config.get('ME', 'level2'))
        ))
        level_2.click()
        level_2.send_keys("sasi@yopmail.com")
        ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ME', 'save_button')))).click()
        time.sleep(1)
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ME', 'okay_bt')))).click()
        time.sleep(1)
        ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ME', 'manage_users1')))).click()

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ME', 'add_user')))).click()
        ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ME', 'save_button')))).click()

        self.driver.save_screenshot("/home/adminroot/Python_Workspace/ICLEAF_21/screenshots/create_CorpCourse5.png")# Wait for the specific div to be visible
        parent_div = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, config.get('ME', 'message2_f'))))

        # Find the span element inside the parent div
        message_element = parent_div.find_element(By.XPATH, config.get('ME', 'message2_c'))

        # Extract the text content from the span element
        message_text = message_element.text

        print("Pop-up Message:", message_text)
        self.driver.save_screenshot("/home/adminroot/Python_Workspace/ICLEAF_21/screenshots/create_CorpCourse5.png")
        time.sleep(1)
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ME', 'okay_bt')))).click()

