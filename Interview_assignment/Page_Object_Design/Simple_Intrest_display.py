from selenium.webdriver import ActionChains


class ShowSI:
    def __init__(self, driver):
        self.driver=driver

        self.financial_tab_by_linktext = "Financial"
        self.display_simple_intrest_xpath ="//div/a[text()='Simple Interest Calculator']"
    def select_financial_tab(self):
        action = ActionChains(self.driver)
        Financial = self.driver.find_element_by_link_text(self.financial_tab_by_linktext)
        action.double_click(Financial).perform()

    def Show_Simple_interest(self):
        self.driver.find_element_by_xpath(self.display_simple_intrest_xpath).is_displayed()
