# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:14:57 2024

@author: Riartts
"""

from pdfminer.high_level import extract_text

texto = extract_text('fatura-luz.pdf')

print(texto)

