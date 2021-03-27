from time import sleep

from selenium import webdriver
import pytest
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.usefixtures("OneTimeSetUp")
class TestCalculateStuff:

    def test_simple_interest_display(self):
        action = ActionChains(self.driver)
        Financial = self.driver.find_element_by_link_text("Financial")
        action.double_click(Financial).perform()
        is_dilpayed = self.driver.find_element_by_xpath("//div/a[text()='Simple Interest Calculator']").is_displayed()

        assert  True==is_dilpayed

    def test_Simple_intrest_claculate(self):
        # action = ActionChains(self.driver)
        #
        # Financial = self.driver.find_element_by_link_text("Financial")
        #
        # action.double_click(Financial).perform()

        self.driver.find_element_by_xpath("//div/a[text()='Simple Interest Calculator']").click()

        self.driver.find_element_by_name("principal").clear()

        self.driver.find_element_by_name("interest_rate").clear()
        self.driver.find_element_by_name("term").clear()


        self.driver.find_element_by_name("principal").send_keys(5000)
        self.driver.find_element_by_name("interest_rate").send_keys(5)
        self.driver.find_element_by_name("term").send_keys(8)

        self.driver.find_element_by_name("commit").click()

        sleep(5)
        Result = self.driver.find_element_by_xpath("(//div[@class='col-xs-4'])[2]")
        Expected_Result = Result.text
        Expected_Simple_Interest ="$2,000.00"

        assert Expected_Simple_Interest==Expected_Result

