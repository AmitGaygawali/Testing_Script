from selenium.webdriver import ActionChains


class CalculateSI:
    def __init__(self, driver):
        self.driver= driver
        self.click_SI_byxpath    ="//div/a[text()='Simple Interest Calculator']"
        self.principle_byname    ="principal"
        self.intrest_rate_byname ="interest_rate"
        self.duration_byname     ="term"
        self.enter_byname        = "commit"
        self.print_byxpath       = "(//div[@class='col-xs-4'])[2]"

    def click_si(self):
        action = ActionChains(self.driver)
        Select_SI_tab = self.driver.find_element_by_xpath(self.click_SI_byxpath)
        action.move_to_element(Select_SI_tab).click().perform()
    def Clear_field(self):
        self.driver.find_element_by_name(self.principle_byname).clear()
        self.driver.find_element_by_name(self.intrest_rate_byname).clear()
        self.driver.find_element_by_name(self.duration_byname).clear()


    def Insert_values(self,principle, intrest,term):

        self.driver.find_element_by_name(self.principle_byname).send_keys(principle)
        self.driver.find_element_by_name(self.intrest_rate_byname).send_keys(intrest)
        self.driver.find_element_by_name(self.duration_byname).send_keys(term)

    def enter(self):
        self.driver.find_element_by_name(self.enter_byname).click()

    def print_result(self):
        Expected_SI = self.driver.find_element_by_xpath(self.print_byxpath)
        print(Expected_SI.text)