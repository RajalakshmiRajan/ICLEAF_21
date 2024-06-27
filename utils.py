
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser



config=configparser.RawConfigParser()
config.read('config.properties')
class WebPageUtils:
    def __init__(self, driver):
        self.driver = driver

    def scroll(self, by, value):
        element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((by, value)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    def url_display(self):
        #elems = self.driver.find_elements(By.XPATH, "//a[@href]")
        elems = self.driver.find_elements(By.XPATH,config.get('ME', 'links_xpath'))
        for elem in elems:
            print(elem.get_attribute("href"))
        print('links')
