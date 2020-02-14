#import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import os
driver=webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win2\chromedriver")
#driver.get("http://mail.google.com/")
driver.get("http://demo.guru99.com/v1/")
print(driver.title)
time.sleep(3)
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@name='uid']").send_keys("Arun")
password=os.environ.get("my_passwd")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
#driver.find_element(By.XPATH, "//input[@name='btnLogin')").click()
driver.find_element(By.XPATH, "//*[@class='dropdown-toggle']").click()

# time.sleep(30)
time.sleep(5)
driver.close()


