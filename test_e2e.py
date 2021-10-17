import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# @pytest.mark.usefixtures("setup")
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        # self.driver.find_element_by_css_selector("a[href*='shop']").click()
        # checkoutPage = CheckoutPage(self.driver)
        log.info("Getting all the card details")
        cards = checkoutPage.getCardTittles()
        # self.driver.find_elements_by_css_selector(".card-title a")
        i = -1
        for card in cards:
            i = i+1
            cardText = card.text
            log.info(cardText)
            if cardText == 'Blackberry':
                # self.driver.find_elements_by_css_selector(".card-footer button")[i].click()
                checkoutPage.getCardFooters()[i].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()

        # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        # checkoutPage.checkOutItems().click()
        confirmPage = checkoutPage.checkOutItems()
        log.info("Entering country name as ind")
        self.driver.find_element_by_id("country").send_keys("ind")
        # time.sleep(5)
        self.verifyLinkPresence("India")

        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text
        log.info("Text received from application is "+textMatch)

        assert ("Success! Thank you!" in textMatch)




