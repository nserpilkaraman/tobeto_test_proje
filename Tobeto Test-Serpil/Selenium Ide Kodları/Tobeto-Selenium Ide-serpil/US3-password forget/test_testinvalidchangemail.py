# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestinvalidchangemail():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testinvalidchangemail(self):
    self.driver.get("https://tobeto.com/sifremi-unuttum")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.CSS_SELECTOR, ".form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys("sxhahxabsch")
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Girdiğiniz e-posta geçersizdir."
  
