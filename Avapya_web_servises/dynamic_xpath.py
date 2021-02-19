from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert



driver = webdriver.Chrome(executable_path="C:/Users/gaiga/OneDrive/Desktop/chromedriver88/chromedriver.exe")

driver.get("https://www.facebook.com/")
driver.maximize_window()

username = driver.find_element(By.ID,"email").send_keys("adgsweetlily@gmail.com")
passward = driver.find_element(By.ID,"pass").send_keys("akashamit16593")
enterbuton = driver.find_element(By.NAME,"login").click()

wait = WebDriverWait(driver,10).until(EC.alert_is_present)
driver.switch_to_alert().accept()


driver.close()