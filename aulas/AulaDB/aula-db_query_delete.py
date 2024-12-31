import os
os.chdir(r'C:\Users\Riartts\OneDrive\Documentos\github\PythonRPA\aulas\AulaDB')
import sqlite3
conn = sqlite3.connect('meubanco.db')
cursor = conn.cursor()


cursor.execute(" DELETE FROM TB_Cliente WHERE CPF = 17746689876")

conn.commit()


