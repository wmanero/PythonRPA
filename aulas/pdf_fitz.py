# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:47:54 2024

@author: Riartts
"""

import fitz

pdf = fitz.open("fatura-luz.pdf")

page = pdf.load_page(0)

texto = page.get_text()

print(texto) 