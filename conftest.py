import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Input language")

@pytest.fixture()
def browser(request):
    my_language = request.config.getoption("--language")
    if not my_language:
        raise pytest.UsageError("set --language!!")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': my_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    #time.sleep(5)
    browser.quit()