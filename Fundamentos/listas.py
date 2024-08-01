# lista = ["p","y","t","h","o","n"]

# # print(lista[2:])
# # print(lista[:2])
# # print(lista[1:3])
# # print(lista[0:3:2])
# # print(lista[::])
# # print(lista[::-1])

# # for n in lista:
# #     print(n)

# for indice, e in enumerate(lista):
#     print(f"{indice}: {e}")


# #compreensão de listas #modo_um
# numeros = [1,30,21,2,9,65,34]
# pares = []

# for numero in numeros:
#     if numero % 2 ==0:
#         pares.append(numero)
# print(pares)
# #1º retorno 2º a iteração 3º filter
# pares_dois =[numero for numero in numeros if numero %2 ==0]

# #modificando valor
# quadrado = []
# for numero in numeros:
#     quadrado.append(numero **2)
# print(quadrado)
# #outra forma
# quadrado_dois = [numero**2 for numero in numeros]
# print(quadrado_dois)

#lista.append(elemento q que adicionar)
#lista.clear() #quando se quer limpar a lista
#lista.copy() # retorna uma instância com a cópia dos valores
#l2 = lista.copy() # terão ID diferentes
#.count # quantas vezes determinado objeto aparece
#.extend # juntar outras listas, novos elementos
linguagens = ["python","java"]
linguagens.extend(["java","c"])
# print(linguagens)
#.index(objeto) #qual primeira ocorrencia do objeto pesquisado
# print(linguagens.index("java"))
#.pop #lista ja vem organizado como pilha, tira o ultimo elemento
#se passar o indice como parâmetro ele remove de forma específica
linguagens.pop(0)
#print(linguagens)
#.remove("objeto") # passa o objeto como parâmetro
linguagens.remove("c")
print(linguagens)
#.reverse # torna a alista ao contrario

#.sort() #ordena a lista
#.sort(reverse=True) ~ faz espelhamento da ordenação
#.sort(key=lambda x: len(x)) # ordem crescente
#.sort(key=lambda x: len(x), reverse=True)
# len(linguagens) # quantidade de elementos
print(len(linguagens))
#sorted(linguagen) # ordenar iteráveis

