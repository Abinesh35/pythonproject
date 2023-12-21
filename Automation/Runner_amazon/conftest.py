import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome"])
def Launch123(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("un supported browser")
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    driver.implicitly_wait(10)
    yield driver

