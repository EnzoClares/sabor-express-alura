pessoa = {'nome': 'cleber', 'idade': 40, 'cidade': 'bélem'}

if 'nome' in pessoa:
  print('a chave nome está presente no dicionário pessoa')
else:
  print('a chava nome não está presente no dicionário')


#atualização de idade: 

pessoa['idade'] = 50



#adicionar um parametro

pessoa['profissão'] = 'desenvolvedor'



# deletando parametro

del pessoa['cidade']


numeros_quadrados = {x:x**2 for x in range(1, 11)}


frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)

