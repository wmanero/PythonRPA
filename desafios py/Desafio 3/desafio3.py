# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 20:11:11 2024

@author: Welton Silva
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from xlsxwriter import workbook
import os
import time

#Invoca o método By
from selenium.webdriver.common.by import By

s_dir = Service(r"C:\\webdriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s_dir)
driver.get("https://concla.ibge.gov.br/busca-online-cnae.html?view=estrutura")
driver.maximize_window()

#seção
driver.find_element(By.XPATH, '//*[@id="tbEstrutura"]/thead/tr/th[1]').location_once_scrolled_into_view
time.sleep(2)
print(driver.find_element(By.XPATH, '//*[@id="tbEstrutura"]/tbody/tr[1]/td[1]/a').text)
driver.find_element(By.XPATH, '//*[@id="tbEstrutura"]/tbody/tr[1]/td[1]/a').click()
time.sleep(2)

#divisão 01
driver.find_element(By.XPATH, '//*[@id="hierarquia"]/table/tbody/tr[1]/td[1]/span').location_once_scrolled_into_view
time.sleep(2)
print(driver.find_element(By.XPATH, '//*[@id="hierarquia"]/table/tbody/tr[2]/td[3]/a').text)
driver.find_element(By.XPATH, '//*[@id="hierarquia"]/table/tbody/tr[2]/td[3]/a').click()
time.sleep(2)

#divisão 02
driver.find_element(By.XPATH, '//*[@id="hierarquia"]/table/tbody/tr[1]/td[1]/span').location_once_scrolled_into_view
time.sleep(2)
print(driver.find_element(By.XPATH, '//*[@id="hierarquia"]/table/tbody/tr[3]/td[3]/a').text)
driver.find_element(By.XPATH, '//*[@id="hierarquia"]/table/tbody/tr[3]/td[3]/a').click()
time.sleep(2)

#grupo
driver.find_element(By.XPATH, '//*[@id="hierarquia"]/table/tbody/tr[1]/td[1]/span').location_once_scrolled_into_view
time.sleep(2)
print(driver.find_element(By.XPATH, '//*[@id="hierarquia"]/table/tbody/tr[4]/td[3]/a').text)
driver.find_element(By.XPATH, '//*[@id="hierarquia"]/table/tbody/tr[4]/td[3]/a').click()
time.sleep(2)

#classe
driver.find_element(By.XPATH, '//*[@id="hierarquia"]/table/tbody/tr[5]/td[1]/span').location_once_scrolled_into_view
time.sleep(2)
print(driver.find_element(By.XPATH, '//*[@id="hierarquia"]/table/tbody/tr[5]/td[3]/a').text)
driver.find_element(By.XPATH, '//*[@id="hierarquia"]/table/tbody/tr[5]/td[3]/a').click()
time.sleep(2)

#subclasse
driver.find_element(By.XPATH, '//*[@id="hierarquia"]/table/tbody/tr[5]/td[1]/span').location_once_scrolled_into_view
time.sleep(2)
print(driver.find_element(By.XPATH, '//*[@id="hierarquia"]/table/tbody/tr[5]/td[3]/span').text)

driver.quit()
