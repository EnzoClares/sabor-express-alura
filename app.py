import os # importando uma biblioteca python
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

def escolher_opcoes():
    opcao_escolhida = int(input('escolha uma opção: '))
    print(f'a opção escolhida foi {opcao_escolhida}')
    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('listar restaurante')
    elif opcao_escolhida == 3:
        print('ativar restaurante')
    else:
        finalizar_app()  

def main():
    mostrar_titulo()
    mostrar_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()