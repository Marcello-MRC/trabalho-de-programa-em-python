lista_alunos = []

while True:
    nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ")
    
   
    if nome == 'fim':
        break  
    
    lista_alunos.append(nome)
    print(lista_alunos)