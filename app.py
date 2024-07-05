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
    limpar_e_por_titulo('finalizando app')

def limpar_e_por_titulo(titulo):
   os.system('cls')
   #os.system('clear') --> para MAC
   print(titulo)
   print()

def voltar_ao_menu_principal():
   input('\nDigite qualquer tecla para voltar ao menu principal: ')
   main()

def opcao_invalida():
  print('Opção Inválida !!!')
  voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    limpar_e_por_titulo('Cadastro de restaurantes novos')
    restaurante_nome = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(restaurante_nome)
    print(f'O restaurante {restaurante_nome} foi cadastrato com sucesso!!\n')
    voltar_ao_menu_principal()

def listar_restaurante():
    limpar_e_por_titulo('listando restaurantes')
    #para cada restaurante na lista de restaurantes
    for restaurante in restaurantes:
       print(f'.{restaurante}')

    voltar_ao_menu_principal()

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