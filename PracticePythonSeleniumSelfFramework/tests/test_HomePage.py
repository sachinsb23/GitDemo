import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from PageObject.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClassA


class TestHomePage(BaseClassA):

    def test_formSubmission(self, getData):

        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()


    @pytest.fixture(params=HomePageData.test_HomePage_Data)
    def getData(self, request):
        return request.param

