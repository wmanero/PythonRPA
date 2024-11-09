# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 21:43:36 2024

@author: wmanero
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


s_dir = Service("C:\Users\Riartts\OneDrive\Documentos\Curso RPA\Python\webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=s_dir)
driver.get("https://www.google.com.br")
driver.maximize_window()



#Invoca o método By
from selenium.webdriver.common.by import By

#Insere palavra Python na caixa de pesquisa.
driver.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys("Python")
#Limpar texto
#driver.find_element(By.XPATH,'//*[@id="APjFqb"]').clear()
#Clica em Enter.
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").submit()
#Clica no link Vídeos do menu.
driver.find_element(By.XPATH, '//div[@class="YmvwI"] [text()="Vídeos"]').click()
#Rola tela para baixo até o texto "Outras".
driver.find_element(By.XPATH, '//*[@class="mgAbYb OSrXXb RES9jf IFnjPb"]').location_once_scrolled_into_view
#Salva print da tela
driver.save_screenshot("google.png")
driver.quit()


