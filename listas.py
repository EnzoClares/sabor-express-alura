numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'joão'];
nomes = ['joão', 'pedro', 'davi', 'simão'];
anos = [2004, 2024];


#soma de números pares
soma_impares = 0
for i in range(1, 11, 2):
  soma_impares += i
print(soma_impares) 


#contagem decrescente
for c in range(10, 0, -1):
  print(c)

#tabuada
numero_escolhido = int(input('Digite um número e veja a tabuada dele: '))

for i in range(1, 11):
  tabuada = i * numero_escolhido
  print(f'{numero_escolhido} X {i} = {tabuada}')

#exceptions

soma = 0 

try: 
  for numero in numeros:
    soma += numero
  print(f'A soma dos elementos é {soma}')
except Exception as e:
  print(f'ocorreu um erro: {e}') 
 
#ZeroDivisorErrors
lista_de_valores = []

try: 
  soma = 0
  for valores in lista_de_valores:
    soma+=valores
  media = soma/len(lista_de_valores)
  print(f'A média dos valores é: {media}')
except ZeroDivisionError:
  print('A lista está vazia, não há como fazer a média')
except Exception as e:
  print(f'ocorreu um erro: {e}')