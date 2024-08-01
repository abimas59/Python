#Conjunto
# set Coleção que não possui objetos repetidos
# ordem de inserção não é garantida
print(set([1,2,3,4,1,2,3,4]))
lista =[1,2,3,4,1,2,3,4]
print(set(lista))
print(set(("palio","gol","palio","celta")))
#não suportam indexação
numeros = {1,2,3,4,2,3,5,4}
#conversão para list
numeros = list(numeros)
print(numeros[0])
##.union ~ 
conjunto_a = {1,2} 
conjunto_b ={2,3,4}
print(conjunto_a.union(conjunto_b))
#.intersection ~ 
print(conjunto_a.intersection(conjunto_b))
#.difference
print(conjunto_a.difference(conjunto_b))
#.symmetric_difference ~ numeros fora da interseção
print(conjunto_a.symmetric_difference(conjunto_b))
#.issubset ~ está contido
#.issuperset ~contem
#.isdisjoint ~ todos elementos de um não está no outro
#.add ~ adicionar um elemento caso não exista 
#.clear ~ limpar
#.copy ~ gera uma cópia
#.discard ~ descartar um valor, não da erro se não tiver
numero = {1,2,3,4,5,3,5,3,2,5}
numero.discard(2)
print(numero)
#.pop remove o primeiro// tipo fila
#.remove ~ remove o passado por parâmetro, se não existir 
#o elemento dará erro
# len(numero) tamanho do conjunto sem duplicados
print(len(numero))