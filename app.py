import os # importando uma biblioteca python

restaurantes = ['pizza', 'sushi']


def mostrar_titulo():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      '''
)#\n cria um break ''' aspas triplas pula linha

def mostrar_opcoes():
    print('1. cadastrar restaurante')
    print('2. listar restaurante')
    print('3. ativar restaurante')
    print('4. sair\n')

def finalizar_app():
    os.system('cls')
    #os.system('clear') --> para MAC
    print('finalizando aplicativo\n')

def opcao_invalida():
  print('Opção Inválida !!!')
  input('Digite qualquer tecla para retornar ao menu\n')
  main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novo restaurante')
    restaurante_nome = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(restaurante_nome)
    print(f'O restaurante {restaurante_nome} foi cadastrato com sucesso!!\n')
    input('\nDigite qualquer tecla para voltar ao menu\n')
    main()

def listar_restaurante():
    os.system('cls')
    print('listando restaurantes\n')
    #para cada restaurante na lista de restaurantes
    for restaurante in restaurantes:
       print(f'.{restaurante}')

    input('\nDigite qualquer tecla para voltar ao menu\n')
    main()

def escolher_opcoes():
    opcao_escolhida = int(input('escolha uma opção: '))
    print(f'a opção escolhida foi {opcao_escolhida}')
    try:
        if opcao_escolhida == 1:
          cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
          listar_restaurante()
        elif opcao_escolhida == 3:
          print('ativar restaurante')
        elif opcao_escolhida == 4:
          finalizar_app()  
        else: 
          opcao_invalida()
    except:
       opcao_invalida()

def main():
    os.system('cls')
    mostrar_titulo()
    mostrar_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()