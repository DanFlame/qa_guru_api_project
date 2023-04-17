import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options

from utils import attach
from utils.base_session import BaseSession

load_dotenv()
api_url_demoshop = os.getenv("API_URL_DEMOSHOP")
print(api_url_demoshop)
api_url_reqres = os.getenv("API_URL_REQRES")
print(api_url_reqres)
email = os.getenv("EMAIL")
print(email)
password = os.getenv("PASSWORD")
print(password)
web_url = os.getenv("WEB_URL_DEMOSHOP")
print(web_url)


@pytest.fixture(scope="session")
def demoshop():
    demoshop_session = BaseSession(api_url_demoshop)
    return demoshop_session


@pytest.fixture(scope="session")
def reqres():
    reqres_session = BaseSession(api_url_reqres)
    return reqres_session


@pytest.fixture(scope='function', autouse=False)
def setup_chrome(demoshop):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = web_url
    response = demoshop.post(url="/login",
                             json={
                                 "Email": email,
                                 "Password": password
                             },
                             allow_redirects=False
                             )
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.open("/Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})

    yield browser
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    browser.quit()
