import pandas as pd

   
data = {
    'Nome': ['Ian Gabriel Braga Trinta', 'Lucas Cisne Cunha', 'Arthur Fernandes Firmeza Felicio', 'Vivian', 'Amanda', 'Rafael', 'Vanessa', 'Arthur Uchôa Diniz', 'Rafaela Pitanga', 'Giovana Oliveira', 'Brenda Guerra', 'Eduarda Araújo', 'Vitor Regis', 'Ronald de Oliveira Martins', 'Maria Luísa Brandão de Luna Barros', 'Rayane', 'Mariana Miranda', 'Yanka', 'Manuela Pitanga', 'Maria Júlia', 'Júlia Camara', 'Guilherme Delgado', 'Ana Júlia', 'João Vitor', 'Kael Cavalcanti', 'Rafaella Lopes', 'caio rezende', 'Pedro Sayão', 'Matheus Costa Real', 'Beatriz Cavalcante', 'José Roberto', 'Gabriel Buarque', 'Yasmin', 'Paulo', 'Tereza Maria Braga Guimarães', 'Ananda Maria', 'Jade Nascimento', 'Alanis Aguiar', 'Samyra', 'Rebecca', 'Isabela', 'Maria Grieser', 'Aline Mell', 'Júlia Choairy', 'Alanna Passos', 'Paulo Arthur', 'Iana Brandão', 'Thomaz Bruhn da Silva', 'Ivan Callado Bezerra de Menezes', 'Sergio Marques Madeira Barros Neto', 'Luiz Eduardo Schmalz', 'Guilherme Satiro', 'Marcello Coimbra de Castro Neto', 'Gustavo', 'Maria Clara Batalha Gonçalves', 'Thomas', 'Anny', 'Cecília', 'Halima', 'Renê Gibran', 'Felipe Neiva de Lima Santos', 'Vivian', 'Julia Naomi', 'Caio Fernandes', 'Gabriela Bezerra'],
    'Idade': [20, 20, 18, 18, 29, 27, 30, 22, 22, 21, 26 , 21, 22, 20, 21, 26, 27, 27, 17, 18, 18, 17, 22, 22, 18, 17, 23, 17, 22, 23, 17, 17, 27, 21, 13, 18, 20, 18, 18, 18, 18, 18, 20, 21, 21, 21, 20, 16, 19, 24, 20, 18, 20, 14, 13, 14, 14, 14, 14, 24, 20, 18, 20, 20, 18],
    'Duração do sono': [9, 7, 8, 7, 8, 7, 7, 6, 8, 5, 7, 7, 8, 7, 8, 6, 7, 9, 11, 8, 7, 9, 6, 7, 5, 5, 6, 8, 6, 6, 7, 7, 9, 6, 5, 8, 8, 7, 6, 5, 8, 6, 8, 7, 6, 6, 6, 7, 8, 7, 9, 9, 8, 6, 7, 8, 7, 8, 6, 7, 8, 7, 8, 7, 6],
    'Em que horário dorme': [22.5, 0, 23, 22, 22, 23, 21, 0, 22, 21.5, 2, 0.5, 22, 1, 23, 0, 23, 21.5, 2, 23, 0, 23, 22, 2, 1, 0, 22.5, 0, 23, 23, 2, 22, 0, 0, 0.5, 3, 22, 23, 23, 23, 1, 22, 21, 23, 0, 0, 23, 0, 23, 1.5, 1, 23, 23, 0, 23, 22.5, 23, 0, 2, 1, 1, 22, 22, 1, 0],
    'Uso diário de celular': [4, 5, 6, 5, 5, 6, 4, 7, 4, 5, 6, 7, 5, 6, 4, 8, 7, 5, 7, 7, 5, 7, 5, 8, 5, 7, 7, 7, 6, 5, 7, 7, 3, 6, 6, 6, 8, 7, 3, 4, 6, 4, 3, 9, 3, 7, 4, 6, 6, 4, 6, 6, 4, 6, 6, 9, 12, 6, 8 , 5, 6, 5, 8, 7, 5],
    'Pratica atividade física regularmente?': [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    'Nível de Stress': [1, 2, 0, 1, 2, 2, 0, 2, 1, 2, 0, 1, 0, 2, 1, 1, 1, 1, 0, 1, 0, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 0, 1, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 2],
    'Disposição ao acordar': ['Alta', 'Média', 'Alta', 'Média', 'Baixa', 'Baixa', 'Baixa', 'Baixa', 'Média', 'Baixa', 'Média', 'Baixa', 'Média', 'Baixa', 'Baixa', 'Média', 'Média', 'Média', 'Alta', 'Baixa', 'Média', 'Média', 'Baixa', 'Média', 'Baixa', 'Média', 'Baixa', 'Alta', 'Média', 'Média', 'Baixa', 'Baixa', 'Média', 'Baixa', 'Baixa', 'Baixa', 'Baixa', 'Média', 'Média', 'Baixa', 'Baixa', 'Média', 'Baixa', 'Média', 'Baixa', 'Baixa', 'Média', 'Média', 'Média', 'Média', 'Média', 'Baixa', 'Média', 'Média', 'Baixa' ,'Média', 'Baixa', 'Média', 'Baixa', 'Média', 'Baixa', 'Média', 'Média', 'Média', 'Baixa'],
}

df = pd.DataFrame(data)

print(df)

df.to_csv('sleep_data.csv', index=False)
