# #bloco de codigo, com conjunto de entrada e de saída
# #pode retornar vários valores
# #retorna none por pedrão
# #programar baseado em funções é a programação de maneira estruturada
# def exibir_mensagem(x):
#     antecessor = x-1
#     sucessor = x +1
#     return antecessor, sucessor
# def exibir_mensagem_2(nome="Anônimo"):
#     print(f"Seja bem vindo {nome}!")

# print(exibir_mensagem(5))

# #exibir_mensagem_2(nome="João")

# #argumentos nomeados
# def salvar_carro(marca,modelo,ano,placa):
#     print(f"Carro inserido com sucesso! {marca}|{modelo}|{ano}|{placa}")

# salvar_carro(marca="Fiat",modelo="Palio",ano=1999,placa="ABS-1234")
# #passando um dicionario, e é convertido para  o de cima
# salvar_carro(**{marca:"Fiat",modelo:"Palio",ano:1999,placa:"ABS-1234"})
#args e kwargs ~ *args e **kwargs
#o método recebe os valores como tupla e dicionario respectivamente.
#se colocar ** vai receber kwargs(dicionario), se * args(tupla)

def exibir_poema(data_extenso, *args, **kwargs):#ou **dicionarios, ou qualquer nome
    texto ="\n".join(args)
    meta_dados="\n".join([f"{chave.title()}:{valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
   # print(mensagem)

exibir_poema("Quinta-feira, 01 de Agosto de 2024","Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)

#parametros nomeais quando se passa com nome chave valor
#parametros posicionais só com a posição
#antes da / só posicionais depois da / nomeados ou posicionais
#def criar_carro(modelo,ano,placa,/,marca,motor, combustivel):
    #print(modelo,ano, placa, marca, motor, combustivel)

#criar_carro("Palio",1999,"ABC-1234",marca="Fiat",motor="1.0",combustivel="Gasolina")
#criar_carro("Palio",1999,"ABC-1234","Fiat","1.0",combustivel="Gasolina")

#só por nome keyword only
#def criar_carro(*,modelo,ano,placa,marca,motor, combustivel):
    #print(modelo,ano, placa, marca, motor, combustivel)
#modo invalido pq não tem os nomes
#criar_carro("Palio",1999,"ABC-1234",marca="Fiat",motor="1.0",combustivel="Gasolina")
#modelo válido só com os nomes
#criar_carro(modelo="Palio",ano=1999,placa="ABC-1234",marca="Fiat",motor="1.0",combustivel="Gasolina")

#keyword and positional only ~ hibrido
def criar_carro_2(modelo,ano,placa,/,marca,*,motor, combustivel):
    print(modelo,ano, placa, marca, motor, combustivel)

#criar_carro_2("Palio",1999,"ABC-1234","Fiat",motor="1.0",combustivel="Gasolina")

#objeto de primeira classe
#obj q pode ser passado por parametro, retornado por uma função
#pode ser passado para variável
def somar(a,b):
    return a+b
def subtrair(a,b):
    return a-b
def exibir_resultado(a,b,funcao):
    resutado = funcao(a,b)
    print(f"o resultado é {a} + {b} = {resutado}")

exibir_resultado(10,10,somar)
exibir_resultado(10,10,subtrair)
op = somar
print(op(1,20))

#escopo local e escopo global
#para usar objetos globais utilizamos a palavra chave global
#mas não é uma boa prática, pois dificulta o debug
salario = 2000
def salario_bonus(bonus):
    global salario
    salario+= bonus
    return salario
salario_bonus(500)
print(salario)