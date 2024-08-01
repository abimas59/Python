# PI = 3.14159
# #tamanho. numero de casas idef(espaços antes) e + o numero de casas
# print(f"Valor de pi: {PI:10.2f}")
dados = {"nome":"Abimael", "idade": 29}
nome = "Abimael"
idade = 29
profissao = "Programador"
linguagem = "Python"
saldo = 50.503
print("Nome:%s Idade:%d "%(nome,idade))
print("Nome:{} Idade:{} ".format(nome,idade))
print("Nome:{0} Idade:{1} outra idade {1}".format(nome,idade)) #ilimitadas chamadas de variavel
print("Nome:{name} Idade:{age} ".format(name=nome,age=idade))
print("Nome:{nome} Idade:{idade} ".format(**dados))
print(f"Nome:{nome} Idade:{idade} ")
print(f"Saldo:{saldo:10.1f}")
