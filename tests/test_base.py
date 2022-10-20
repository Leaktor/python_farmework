import time


def test_base(driver, age_gate, catalog):
    driver.get("https://iqos.ru/shop/iqos/")
    age_gate.set_age("10101991")
    age_gate.confirm_button_click()
    age_gate.accept_button_click()
    catalog.scroll_to_view()
    assert catalog.check_visibility() == True

