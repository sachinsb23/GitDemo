from selenium.webdriver.common.by import By

from PageObject.ConfirmationPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    # cards = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    # self.driver.find_elements_by_css_selector(".card-footer button")[i].click()
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage


