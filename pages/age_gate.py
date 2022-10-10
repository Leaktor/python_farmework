import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.test_element import TestElement

# Этот пейдж создан исключительно для тестирования фрейма. При использовании фрейма этот пейдж нужно удалить

class AgeGate(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.age_gate_input = TestElement(self.driver, '//*[contains(@class,"parent-input-error")]')
        self.confirm_button = TestElement(self.driver, '//*[contains(@class,"btn-confirm")]')

    def set_age(self, age):
        try:
            time.sleep(5)
            print(self.age_gate_input.get_locator())
            self.age_gate_input.click()
            for character in age:
                self.age_gate_input.send_keys(character)
        except:
            print("something wrong happened")
        return self

    def confirm_button_click(self):
        self.confirm_button.click()

    def accept_button_click(self):
        accept_button = self.driver.find_element(By.XPATH,
                                                 '//*[contains(@id,"onetrust-accept-btn-handler")]')
        accept_button.click()
