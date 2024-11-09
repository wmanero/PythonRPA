# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:43:31 2024

@author: Riartts
"""

import pdfplumber

arqv_pdf = pdfplumber.open("fatura-luz.pdf")

page = arqv_pdf.pages[0]

texto = page.extract_text()

print(texto)