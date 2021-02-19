from selenium import webdriver
from selenium.webdriver.common import action_chains
import pytest

@pytest.mark.usefixtures("OneTimeSetUp")
class TestWebsite:

    def test_wbsite_launch(self):
        assert True