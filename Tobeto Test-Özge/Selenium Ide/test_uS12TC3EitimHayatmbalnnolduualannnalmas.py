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

class TestUS12TC3EitimHayatmbalnnolduualannnalmas():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_uS12TC3EitimHayatmbalnnolduualannnalmas(self):
    self.driver.get("https://tobeto.com/giris")
    self.driver.set_window_size(1552, 849)
    element = self.driver.find_element(By.CSS_SELECTOR, ".login")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("ozgecam@outlook.com")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("ozge-cam-5595")
    self.driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()
    self.driver.find_element(By.XPATH, "(//button[@type=\'button\'])[4]").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'__next\']/div/nav/div/div/div/div[2]/button/div[2]/p").click()
    self.driver.find_element(By.XPATH, "//a[contains(text(),\'Profil Bilgileri\')]").click()
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Eğitim Hayatım\')]").click()
    self.driver.close()
  
