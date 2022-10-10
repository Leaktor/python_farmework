import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from webdriver_manager.chrome import ChromeDriverManager

from pages.age_gate import AgeGate
from pages.catalog import Catalog


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_experimental_option("prefs", {
        "download.default_directory": r"C:\Users\xxx\downloads\Test",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    return options


@pytest.fixture
def driver(get_chrome_options):
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=get_chrome_options)
    driver.implicitly_wait(10)
    print("\nstart browser..")
    yield driver
    print("\nquit browser..")
    driver.quit()


@pytest.fixture()
def age_gate(driver):
    return AgeGate(driver)


@pytest.fixture()
def catalog(driver):
    return Catalog(driver)
