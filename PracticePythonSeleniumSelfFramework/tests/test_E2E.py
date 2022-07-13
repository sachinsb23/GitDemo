
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.CheckoutPage import CheckOutPage
from PageObject.HomePage import HomePage
from utilities.BaseClass import BaseClassA
import pdb
import time


class TestOne(BaseClassA):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkOutPage = homepage.shopItems()
        log.info("getting all the card titles")
        cards = checkOutPage.getCardTitles()

        print(cards)
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()

        time.sleep(5)
        self.driver.find_element_by_css_selector(".nav-link.btn.btn-primary").click()

        confirmPage = checkOutPage.checkOutItems()
        log.info("Entering Country Name as India")
        self.driver.find_element_by_id("country").send_keys("ind")
        self.verifyLinkPresence("India")


        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text
        log.info("Text received from application is " +textMatch)

        assert ("Success! Thank you!" in textMatch)
