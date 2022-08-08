from main import cria_descritivo_curso

curso_titulo = input('Qual o título do curso?')
curso_descricao = input('Descreva o curso')
curso_professor = input('Qual é o nome do professor desse curso?')
topico_1 = input('O que você vai aprender na aula 1?')
topico_2 = input('O que você vai aprender na aula 2?')
topico_3 = input('O que você vai aprender na aula 3?')
topico_4 = input('O que você vai aprender na aula 4?')
topico_5 = input('O que você vai aprender na aula 5?')
data_1 = input("Que dia será a aula 1?")
data_2 = input("Que dia será a aula 2?")
data_3 = input("Que dia será a aula 3?")
data_4 = input("Que dia será a aula 4?")
data_5 = input("Que dia será a aula 5?")
arquivo_nome = input('Que nome você quer dar ao arquivo que será gerado?')

cria_descritivo_curso(
    curso_titulo,
    curso_descricao,
    curso_professor,
    topico_1,
    topico_2,
    topico_3,
    topico_4,
    topico_5,
    data_1,
    data_2,
    data_3,
    data_4,
    data_5, 
    arquivo_nome
) 
