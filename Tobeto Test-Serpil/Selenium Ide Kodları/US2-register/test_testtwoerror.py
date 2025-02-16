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

class TestTesttwoerror():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testtwoerror(self):
    self.driver.get("https://tobeto.com/giris")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.CSS_SELECTOR, ".signup").click()
    self.driver.find_element(By.NAME, "firstName").click()
    self.driver.find_element(By.NAME, "firstName").send_keys("pair2")
    self.driver.find_element(By.NAME, "lastName").send_keys("tobeto")
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("pair2tobeto2@gmail.com")
    self.driver.execute_script("window.scrollTo(0,178.39999389648438)")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("123")
    self.driver.find_element(By.NAME, "passwordAgain").click()
    self.driver.find_element(By.NAME, "passwordAgain").send_keys("123")
    self.driver.find_element(By.CSS_SELECTOR, ".mt-4").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".mt-4")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.NAME, "contact").click()
    self.driver.find_element(By.NAME, "membershipContrat").click()
    self.driver.find_element(By.NAME, "emailConfirmation").click()
    self.driver.find_element(By.NAME, "phoneConfirmation").click()
    self.driver.find_element(By.ID, "phoneNumber").click()
    self.driver.find_element(By.ID, "phoneNumber").send_keys("+90 534 608 59 64")
    self.driver.switch_to.frame(8)
    self.driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
    self.driver.switch_to.default_content()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-yes").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".alert-modal").text == "Kayıt oluşturmak için gerekli sözleşmeler\\\\nKişisel verileriniz Aydınlatma Metni kapsamında işlenmektedir.\\\\nAçık Rıza Metni’ni okudum ve anladım.*\\\\nÜyelik Sözleşmesi ve Kullanım Koşulları’nı okudum ve anladım.*\\\\nİletişim bilgilerim üzerinden pazarlama ve tanıtım amaçlı irtibata geçilmesini kabul ediyorum.\\\\nE-posta gönderim izni.*\\\\nArama izni.*\\\\nUluslararası\\\\nAfganistan\\\\nÅland Adaları\\\\nAlmanya\\\\nAmerika Birleşik Devletleri\\\\nAmerikan Samoası\\\\nAndorra\\\\nAngola\\\\nAnguilla\\\\nAntigua ve Barbuda\\\\nArjantin\\\\nArnavutluk\\\\nAruba\\\\nAvustralya\\\\nAvusturya\\\\nAzerbaycan\\\\nAziz Barthélemy\\\\nAziz Helena\\\\nBahamalar\\\\nBahreyn\\\\nBangladeş\\\\nBarbados\\\\nBatı Sahra\\\\nBelçika\\\\nBelize\\\\nBenin\\\\nBermuda\\\\nBeyaz Rusya\\\\nBirleşik Arap Emirlikleri\\\\nBolivya\\\\nBonaire, Sint Eustatius ve Saba\\\\nBosna Hersek\\\\nBotsvana\\\\nBrezilya\\\\nBrunei Darussalam\\\\nBulgaristan\\\\nBurkina Faso\\\\nBurundi\\\\nButan\\\\nCayman Adaları\\\\nCebelitarık\\\\nCezayir\\\\nChristmas Adası\\\\nCibuti\\\\nCocos (Keeling) Adaları\\\\nCook Adaları\\\\nCuraçao\\\\nÇad\\\\nÇek Cumhuriyeti\\\\nÇin\\\\nDanimarka\\\\nDoğu Timor\\\\nDominik Cumhuriyeti\\\\nDominika\\\\nEkvador\\\\nEkvator Ginesi\\\\nEl Salvador\\\\nEndonezya\\\\nEritre\\\\nErmenistan\\\\nEstonya\\\\nEtiyopya\\\\nFalkland Adaları\\\\nFaroe Adaları\\\\nFas\\\\nFiji\\\\nFildişi Sahili\\\\nFilipinler\\\\nFilistin\\\\nFinlandiya\\\\nFransa\\\\nFransız Guyanası\\\\nFransız Polinezyası\\\\nGabon\\\\nGambiya\\\\nGana\\\\nGine\\\\nGine-Bissau\\\\nGrenada\\\\nGrönland\\\\nGuadeloupe\\\\nGuam\\\\nGuatemala\\\\nGuernsey\\\\nGuyana\\\\nGüney Afrika\\\\nGüney Kore\\\\nGüney Sudan\\\\nGürcistan\\\\nHaiti\\\\nHırvatistan\\\\nHindistan\\\'da\\\\nHollanda\\\\nHoly See (Vatikan Şehir Devleti)\\\\nHonduras\\\\nHong Kong\\\\nIrak\\\\nİngiliz Hint Okyanusu Bölgesi\\\\nİngiltere\\\\nİran\\\\nİrlanda\\\\nİspanya\\\\nİsrail\\\\nİsveç\\\\nİsviçre\\\\nİtalya\\\\nİzlanda\\\\nJamaika\\\\nJaponya\\\\nJersey\\\\nKamboçya\\\\nKamerun\\\\nKanada\\\\nKaradağ\\\\nKatar\\\\nKazakistan\\\\nKenya\\\\nKıbrıs\\\\nKırgızistan\\\\nKiribati\\\\nKolombiya\\\\nKomorlar\\\\nKongo\\\\nKongo, Demokratik Cumhuriyeti\\\\nKosova\\\\nKosta Rika\\\\nKuveyt\\\\nKuzey Kore\\\\nKuzey Makedonya\\\\nKuzey Mariana Adaları\\\\nKüba\\\\nLaos\\\\nLesotho\\\\nLetonya\\\\nLiberya\\\\nLibya\\\\nLihtenştayn\\\\nLitvanya\\\\nLübnan\\\\nLüksemburg\\\\nMacaristan\\\\nMadagaskar\\\\nMakao\\\\nMalavi\\\\nMaldivler\\\\nMalezya\\\\nMali\\\\nMalta\\\\nMan Adası\\\\nMarshall Adaları\\\\nMartinik\\\\nMauritius\\\\nMayotte\\\\nMeksika\\\\nMısır\\\\nMikronezya Federal Devletleri\\\\nMoğolistan\\\\nMoldova\\\\nMonako\\\\nMontserrat\\\\nMoritanya\\\\nMozambik\\\\nMyanmar\\\\nNamibya\\\\nNauru\\\\nNepal\\\\nNijer\\\\nNijerya\\\\nNikaragua\\\\nNiue\\\\nNorfolk Adası\\\\nNorveç\\\\nOrta Afrika Cumhuriyeti\\\\nÖzbekistan\\\\nPakistan\\\\nPalau\\\\nPanama\\\\nPapua Yeni Gine\\\\nParaguay\\\\nPeru\\\\nPolonya\\\\nPortekiz\\\\nPorto Riko\\\\nRomanya\\\\nRuanda\\\\nRusya\\\\nSaint Kitts ve Nevis\\\\nSaint Lucia\\\\nSaint Martin (Fransız Bölgesi)\\\\nSaint Pierre ve Miquelon\\\\nSaint Vincent ve Grenadinler\\\\nSamoa\\\\nSan Marino\\\\nSao Tome ve Principe\\\\nSenegal\\\\nSeyşeller\\\\nSırbistan\\\\nSierra Leone\\\\nSingapur\\\\nSint Maarten\\\\nSlovakya\\\\nSlovenya\\\\nSolomon Adaları\\\\nSomali\\\\nSri Lanka\\\\nSudan\\\\nSurinam\\\\nSuriye\\\\nSuudi Arabistan\\\\nSvalbard ve Jan Mayen\\\\nSvaziland\\\\nŞili\\\\nTacikistan\\\\nTanzanya\\\\nTayland\\\\nTayvan\\\\nTogo\\\\nTokelau\\\\nTonga\\\\nTrinidad ve Tobago\\\\nTristan da Cunha\\\\nTunus\\\\nTurks ve Caicos Adaları\\\\nTuvalu\\\\nTürkiye\\\\nTürkmenistan\\\\nUganda\\\\nUkrayna\\\\nUmman\\\\nUruguay\\\\nÜrdün\\\\nVanuatu\\\\nVenezuela\\\\nVietnam\\\\nVirgin Adaları, ABD\\\\nVirgin Adaları, İngiliz\\\\nWallis ve Futuna\\\\nYemen\\\\nYeni Kaledonya\\\\nYeni Zelanda\\\\nYeniden Birleşme\\\\nYeşil Burun Adaları\\\\nYunanistan\\\\nYükseliş Adası\\\\nZambiya\\\\nZimbabve\\\\nKapat\\\\nDevam Et"
  
