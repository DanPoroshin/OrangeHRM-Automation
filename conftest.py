import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(autouse=True, scope="function")
def driver(request):
    options = Options()
    options.add_argument("--headless") # Comment for running on local device
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")


    # Comment for running on local device
    chrome_driver_path = "/usr/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chrome_driver_path
    driver = webdriver.Chrome(options=options, service=webdriver.chrome.service.Service(chrome_driver_path))
    request.cls.driver = driver

    # Uncomment for running on local device
    # driver = webdriver.Chrome(options=options)


    yield driver
    driver.quit()