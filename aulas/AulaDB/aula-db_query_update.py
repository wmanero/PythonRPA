import os
os.chdir(r'C:\Users\Riartts\OneDrive\Documentos\github\PythonRPA\aulas\AulaDB')
import sqlite3
conn = sqlite3.connect('meubanco.db')
cursor = conn.cursor()


cursor.execute("UPDATE TB_Cliente SET Telefone = NULL, Email = NULL WHERE CPF = '901.234.567-00'")

conn.commit()


