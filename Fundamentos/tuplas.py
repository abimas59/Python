# #estruturas de dados parecidas com a lista,
# # diferença que tuplas são imutáveis, tipo uma "constante"
# #podemos criar tuplas através da classe tuple. ou colocando valores separados
# #por virgula dentro de parenteses, lista usa colchetes
# frutas = ("laranja","pera","uva",) #por virgula no final boa pratica
# letras = tuple("python")
# numeros = tuple([1,2,3,4])
# pais = ("Brasil",)
# #mecanismos parecidos com o da lista frutas[0], numeros[-1]
# #é possível armazenar tupla dentro de outras tuplas
# matriz = ( #se for imutável, melhor tupla a lista
#     (1,"a",2),
#     ("b","a",2),
#     (6,4,"C"),
# )
# tupla = ("p","y","t","h","o","n")
# print(tupla[::-1])
# #tem .count
# #tem .index
# #tem o len(tupla)

carros = ("gol",)
print(isinstance(carros, tuple))