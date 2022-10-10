from selenium.webdriver.common.by import By


class TestElement():
    def __init__(self, driver, locator):
        self.driver = driver
        self.explicit_wait = 10
        self.locator = locator
        self.element = lambda: self.driver.find_element(By.XPATH,
                                                        self.locator)

    def get_element(self):
        return self.element()

    def get_locator(self):
        return self.locator

    def scroll_into_center(self):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", self.element())

    def send_keys(self, keys):
        self.element().send_keys(keys)

    def click(self):
        self.element().click()

    def check_exists_by_xpath(self, locator):
        try:
            self.driver.find_element(By.XPATH,
                                     locator)
        except:
            return False
        return True

    def scroll_page_before_element_displayed(self):
        a = 0
        while a < 10:
            if not self.check_exists_by_xpath(self.locator):
                self.driver.execute_script(f"window.scrollTo(0, window.scrollY + {a * 400})")
                a += 1
            else:
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", self.element())
                break
