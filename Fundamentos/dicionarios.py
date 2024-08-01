# #conjunto não ordenado de pares, chave:valor
# pessoa = {"nome":"Abimael", "idade": 28}
# #outra formar de declarar
# pessoa = dict(nome="Abimael", idade=28)
# #já tem o dicionario criado, add novos elementos
#caso já tenha o eleemnto, ele é atualizado
# pessoa["telefone"] ="719999-999"
# pessoa["altura"] = 1.71
# print(pessoa["nome"])
# print(pessoa)

##############
#dicionarios aininhados
contatos = {
    "britt@outlook.ph":{"nome":"Abimael","telefone":"719999999","idade":18},
    "britt@outlook":{"nome":"mael","telefone":"7199999929","idade":181},
}
telefone = contatos["britt@outlook.ph"]["idade"]
#print(telefone)

#forma de iterar
#for chave in contatos:
    #print(chave, contatos[chave])

#mais legível
for chave, valor in contatos.items():
    print(chave, valor)
#caso 