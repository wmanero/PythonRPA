# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 21:01:06 2024

@author: wmanero
"""

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
s_dir = Service(r"C:\Users\Riartts\OneDrive\Documentos\Curso RPA\Python\webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=s_dir)
driver.get("https://google.com")
#driver.maximize_window()
driver.implicitly_wait(30)
#driver.close()

