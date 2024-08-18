import time
import os


pasta_estudantes = 'estudantes'
if not os.path.exists(pasta_estudantes):
    os.makedirs(pasta_estudantes)


# Nesta versão já esta um pouco mais avançado, pois já consigo atualizar o nome do estudante.
# Lista para armazenar os nomes dos estudantes


estudantes = []



def menu_principal():
    while True:
        print("\nMenu Principal")
        print("1. Estudantes")
        print("2. Lista de Estudantes")
        print("3. Professores")
        print("4. Disciplinas")
        print("5. Turmas")
        print("6. Matrículas")
        print("0. Sair")

        opcao = input('Selecione uma opção: ')

        if  opcao == '1':
            menu_estudante()
        elif opcao == 2:
            listar_estudantes()
        elif opcao in ['2','3', '4', '5', '6', ]:
            print('EM DESENVOLVIMENTO')
        elif opcao == 0:
            print('Saindo...')
            break    

        else:
            print('Opção inválida, por favor tente novamente.')

def menu_estudante():
    while True:
        print('\nMenu de operções do estudante.')
        print('1. Cadastrar Estudante.')
        print('2. Atualizar Cadastro.')
        print('3. Excluir Cadastro.')
        print('0. Voltar ao menu principal.')

        opcao = input('Selecione uma opção: ')
            
        if opcao == '1':
                incluir_estudante()
        elif opcao == '2':
                atualizar_estudante()
        elif opcao == '3':
             excluir_estudante()
        elif opcao == '0':
             print('Voltando ao menu principal...')
             time.sleep(2)
             break
        else:
             print('Tente novamente.')


#para incluir um nome a lista de estudantes
def incluir_estudante():
    
     nome = input('Digite o nome do estudante: ')  #adiciona o nome desejado
     with open(os.path.join(pasta_estudantes, 'estudantes.txt'), 'a') as arquivo:
        arquivo.write(nome + '\n')
     estudantes.append(nome)   #Salva o nome escolhido
     print(f'Estudante {nome}, incluido com sucesso.')
     time.sleep(2)



def atualizar_estudante():
    nome = input('Digite o nome do estudante a ser atualizado: ')
    for i in range(len(estudantes)):
        if estudantes[i] == nome:
            novo_nome = input('Digite o novo nome do estudante: ')
            estudantes[i] = novo_nome  # Atualiza o nome na lista
            print(f'Estudante {nome} atualizado com sucesso para {novo_nome}.')
            time.sleep(2)
            return  # Saia da função após a atualização bem-sucedida
    
    # Se o loop terminar sem encontrar o nome, execute este bloco
    print('Estudante não encontrado.')
    time.sleep(2)



               





# para executar o menu principal
menu_principal()                 

