import os # importando uma biblioteca python

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo': True},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':False},
                {'nome':'Cantina', 'categoria':'Italiana', 'ativo':True}]


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
    categoria = input(f'Digite a categoria do restaurante {restaurante_nome}: ')
    dados_do_restaurante = {'nome':restaurante_nome, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {restaurante_nome} foi cadastrato com sucesso!!\n')
    voltar_ao_menu_principal()

def listar_restaurante():
    limpar_e_por_titulo('listando restaurantes')
    #para cada restaurante na lista de restaurantes
    for restaurante in restaurantes:
       restaurante_nome = restaurante['nome']
       restaurante_categoria = restaurante['categoria']
       restaurante_ativo = restaurante['ativo']
       print(f'-{restaurante_nome} | {restaurante_categoria} | {restaurante_ativo}')

    voltar_ao_menu_principal()

def alternando_estado_restaurante():
    limpar_e_por_titulo('Alternar estado do restaurante: ')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
       if nome_restaurante == restaurante['nome']:
          restaurante_encontrado = True
          restaurante['ativo'] = not restaurante['ativo']
          mensagem = f'O restaurante {nome_restaurante} foi Ativado com sucesso'if restaurante['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso'
          print(mensagem)
    if not restaurante_encontrado: 
        print('o restaurante não foi encontrado')
  
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
          alternando_estado_restaurante()
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