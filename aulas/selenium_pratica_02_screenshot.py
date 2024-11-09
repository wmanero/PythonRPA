# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 21:27:48 2024

@author: wmanero
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Invoca o método By
from selenium.webdriver.common.by import By

s_dir = Service(r"C:\Users\Riartts\OneDrive\Documentos\Curso RPA\Python\webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=s_dir)
driver.get("https://www.amazon.com.br")
#driver.refresh()
driver.maximize_window()

#Extraindo texto da página
texto = (driver.find_element(By.XPATH, "//div[@id='nf4ujxnKSeT-7bI4sjUONw']/div/h2").text)
print(texto)

#Extraindo texto do label com get_attribute
texto = (driver.find_element(By.ID, "nav-logo-sprites").get_attribute('aria-label'))
print(texto)

#Screeshot
driver.find_element(By.ID, "nav-xshop-container").screenshot("navebar.png")
driver.find_element(By.ID, "nav-logo").screenshot("logo.png")

#Screeshot tela inteira
driver.save_screenshot("amazon.png")

from selenium.webdriver.support.ui import Select
#Criando variável dropdrown com select 
dropdrown = Select(driver.find_element(By.ID, "searchDropdownBox"))
#dropdrown por texto
dropdrown.select_by_visible_text("Alimentos e Bebidas")
#Dropdrown por value
dropdrown.select_by_value("search-alias=warehouse-deals")
#Dropdrown por index
dropdrown.select_by_index("6")


