import random #biblioteca para ter valores aleatorios e aleatorizar itens em uma lista

naipes = ['Ouro', 'Espadas', 'Copas', 'Paus']#lista de naipes
numeros = ['Ás', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']#lista de numeros

cartas = [] #deck com todas as 52 cartas -> 4 X 13 = 52 combinações
for i in range(4):#range define o tamanho ou quantidade de itens a ser usado
    for u in range(13):
      cartas.append(str(numeros[u])+" de "+naipes[i]) #append adiciona um valor a uma lista, no caso a lista cartas
b = int(input('Qual a quantidade de cartas?\n'))#recebe um valor digitado pelo usuario e joga em uma variavel

random.shuffle(cartas)#pega uma sequência, como uma lista, e reorganiza a ordem dos itens
for i in range(b):
    print(cartas[i])#imprime a carta na posição do contador