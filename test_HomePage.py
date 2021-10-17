import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePgaeData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        ''' driver = webdriver.Chrome(executable_path="C\\chromedriver.exe")
        driver.get("https://rahulshettyacaemy.com/angularpractice/")
        driver.maximize_window() '''  # This will come from BaseClass & Conftest file
        # driver.find_element_by_css_selector("[name='name']").send_keys("Sangeeta")
        homePage = HomePage(self.driver)
        log = self.getLogger()
        log.info("First Name  is "+getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        # driver.find_element_by_name("email").send_keys("Naik")
        log.info("Email  is "+getData["email"])
        homePage.getEmail().send_keys(getData["email"])
        # driver.find_element_by_id("exampleCheck1").click()
        homePage.getCheckBox().click()
        '''sel = Select(driver.find_element_by_id("exampleFormControlSelect1"))
        sel.select_by_visible_text("Female")'''
        # sel = Select(homePage.getGender())
        # sel.select_by_visible_text("Female")  # This code can be reusable.Hence, defined in BaseClass
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        # driver.find_element_by_xpath("//input[@value= 'Submit']").click()
        homePage.submitForm().click()

        # alertText = driver.find_element_by_css_selector("[class*= 'alert-success']").text
        alertText = homePage.getSuccessMessage().text
        print(alertText)
        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params= HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param

