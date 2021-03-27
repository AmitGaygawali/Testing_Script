from time import sleep
import pytest
from Interview_assignment.Page_Object_Design.Simple_Intrest_display import ShowSI
from Interview_assignment.Page_Object_Design.Calculate_SI import CalculateSI
@pytest.mark.usefixtures("OneTimeSetUp")
class TestCalculateStuff:

    def test_show_simple_inrest(self):
        SI = ShowSI(self.driver)
        SI.select_financial_tab()
        SI.Show_Simple_interest()

        assert True
    def test_SI_result(self):
        result = CalculateSI(self.driver)
        result.click_si()
        result.Clear_field ()
        result.Insert_values(5000,8,5)
        result.enter()
        sleep(5)
        result.print_result()

        assert True