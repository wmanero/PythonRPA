import os
os.chdir(r'C:\Users\Riartts\OneDrive\Documentos\github\PythonRPA\aulas\AulaDB')
import sqlite3
conn = sqlite3.connect('meubanco.db')
cursor = conn.cursor()

dados_pessoas = [
    ('123.456.789-00', 'Maria Silva Oliveira', '1985-03-15', '(11) 98765-4321', 'maria.silva@email.com', '01234-567'),
    ('987.654.321-00', 'João Pedro Santos', '1990-08-22', '(21) 99876-5432', 'joao.santos@email.com', '20543-210'),
    ('456.789.123-00', 'Ana Carolina Lima', '1988-11-30', '(31) 97654-3210', 'ana.lima@email.com', '30123-456'),
    ('789.123.456-00', 'Lucas Fernandes Costa', '1995-04-18', '(41) 96543-2109', 'lucas.costa@email.com', '41789-012'),
    ('234.567.890-00', 'Beatriz Almeida Rocha', '1992-07-25', '(51) 95432-1098', 'beatriz.rocha@email.com', '50456-789'),
    ('678.901.234-00', 'Rafael Souza Pereira', '1987-01-10', '(61) 94321-0987', 'rafael.pereira@email.com', '60987-654'),
    ('345.678.901-00', 'Juliana Santos Lima', '1993-09-05', '(71) 93210-9876', 'juliana.lima@email.com', '70234-567'),
    ('890.123.456-00', 'Fernando Costa Silva', '1986-06-20', '(81) 92109-8765', 'fernando.silva@email.com', '80567-890'),
    ('567.890.123-00', 'Camila Oliveira Martins', '1991-12-12', '(91) 91098-7654', 'camila.martins@email.com', '90890-123'),
    ('901.234.567-00', 'Gabriel Pereira Santos', '1989-02-28', '(12) 90987-6543', 'gabriel.santos@email.com', '12345-678')
]

#cursor.execute('''INSERT INTO TB_Cliente VALUES ('17746689876', 'Lauana Prado', '13/06/1948', '68991361938', 'lauanaprado@gmail.com', '04844360')''')
cursor.executemany("INSERT INTO TB_Cliente VALUES (?,?,?,?,?,?)", dados_pessoas)
conn.commit()


