from pages.base_page import BasePage
from pages.test_element import TestElement

# Этот пейдж создан исключительно для тестирования фрейма. При использовании фрейма этот пейдж нужно удалить
class Catalog(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.card_selector = TestElement(self.driver,
                                         "//*[contains(@class,'card-product ddl_prouduct catalog__card')][15]")

    def scroll_to_view(self):
        # self.wait_for_element(self.card_selector.get_element())
        # self.card_selector.get_element().wa
        # self.card_selector.scroll_into_center()
        print(self.card_selector.get_locator())
        self.card_selector.scroll_page_before_element_displayed()
