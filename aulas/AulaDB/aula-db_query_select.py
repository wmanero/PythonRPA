import os
os.chdir(r'C:\Users\Riartts\OneDrive\Documentos\github\PythonRPA\aulas\AulaDB')
import sqlite3
conn = sqlite3.connect('meubanco.db')
cursor = conn.cursor()


cursor.execute("SELECT * FROM TB_Cliente")

resultado = cursor.fetchone() # Traz o primeiro item encontrado na tabela.
resultados = cursor.fetchall() # Traz todos os itens encontrados na tabela.

print('Resultado Fetchone()')
#print(resultado)
print("")
print('Resultado Fetchall()')
#print(resultados)

# Pesquisa por algo específico.

cursor.execute("SELECT * FROM TB_Cliente WHERE Nome_Completo LIKE '%Ana%'")

pesquisa = cursor.fetchall() # Traz todos os registros encontrados na tabela.
print(pesquisa)