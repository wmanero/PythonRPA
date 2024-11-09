from xlsxwriter import Workbook

wb = Workbook('.\\aulas\\livros.xlsx')
planilha = wb.add_worksheet('Livros')

bold = wb.add_format({'bold': 1})
planilha.write('A1', 'Nome', bold)
planilha.write('B1', 'Autor', bold)
planilha.write('C1', 'Data Lançamento', bold)
planilha.write('D1', 'País de Origem', bold)
planilha.write('E1', 'Gênero', bold)


livros = [
    ["Dom Quixote", "Miguel de Cervantes", "1605", "Espanha", "Romance"],
    ["Orgulho e Preconceito", "Jane Austen", "1813", "Reino Unido", "Romance"],
    ["Cem Anos de Solidão", "Gabriel García Márquez", "1967", "Colômbia", "Realismo Mágico"],
    ["O Grande Gatsby", "F. Scott Fitzgerald", "1925", "Estados Unidos", "Romance"],
    ["1984", "George Orwell", "1949", "Reino Unido", "Distopia"]
]

row, col = 1, 0

for livro in livros:
    planilha.write_string(row, col, livro[0])
    planilha.write_string(row, col+1, livro[1])
    planilha.write_string(row, col+2, livro[2])
    planilha.write_string(row, col+3, livro[3])
    planilha.write_string(row, col+4, livro[4])

    row += 1

wb.close()