# from Automation.Homepage.homePage import Home_Page
# from Automation.Runner_amazon import conftesta

from Automation.Homepage.homePage import Homeamazon


def test_amazon(Launch123):
    driver = Launch123
    home = Homeamazon(driver)
    home.search_home()
