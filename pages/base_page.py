from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functools import singledispatch, singledispatchmethod


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.explicit_wait = 10

    def click(self, locator):
        self.wait_for_element_to_be_clickable(locator).click()

    def click_js(self, locator):
        self.driver.execute_script("arguments[0].click();", self.wait_for_element(locator))

    @singledispatchmethod
    def wait_for_element(self, locator):
        pass

    @wait_for_element.register
    def _(self, locator: str):
        print("Локатор", locator)
        return WebDriverWait(self.driver, self.explicit_wait).until(EC.presence_of_element_located((By.XPATH, locator)))

    @wait_for_element.register
    def _(self, element: WebElement):
        print("Элемент", element)
        return WebDriverWait(self.driver, self.explicit_wait).until(EC.visibility_of(element))

    def wait_for_elements(self, locator):
        return WebDriverWait(self.driver, self.explicit_wait).until(EC.presence_of_all_elements_located(locator))

    def wait_for_text_in_element(self, locator, text):
        return WebDriverWait(self.driver, self.explicit_wait).until(EC.text_to_be_present_in_element(locator, text))

    def wait_for_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, self.explicit_wait).until(EC.element_to_be_clickable((By.XPATH, locator)))

    def check_visibility_of_elements(self, locator):
        return WebDriverWait(self.driver, self.explicit_wait).until(EC.visibility_of_all_elements_located(locator))
