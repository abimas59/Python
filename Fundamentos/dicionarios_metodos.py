#.clear ~ apaga tudo do dicionario
#.copy ~ faz uma copia do dic
#.fromkeys ~ cria chaves
dict.fromkeys(["nome","telefone"])
#.fromkeys ~ cria chaves com valor padrão
dict.fromkeys(["nome","telefone"],"vazio")
#ficaria nome:vazio, telefone:vazio
#.get segunda forma de acessar valores no dicionario
# #quando não se tem certeza se a chave existe
# contatos.get("chave")
# #ou retorna vazio, caso nãao encontre
# contatos.get("chave",{})
# #ex
# contatos.get("britt@outlook.ph", {})
# #.items ~retorna uma lista de tuplas
#.keys ~ retorna só as chaves do dicionário
document = {"email":"abimael@live","idade":29,"sexo":"selvagem"}
#print(document.keys())
#.pop remove uma chave do dicionário, passando a chave como param
#ou um valor padrão
#.popitem ~ remove os itens na sequencia, sem precisar apassa parametros
#.setdefault ~ se o atributo não estiver no dicionario, ele vai com o valor padrão
document.setdefault("altura",1.71)
#print(document)
#.update ~ atualiza o dicionario, com outro dicionario
#atualiza as chaves já existentes
document.update({"email":"abimael","idade":9})
#print(document)
#.values ~ todos os dicionários que estão amarrados com as chaves
#todos os valores q o dicinoario tem
# in ~ verifica se a chave esta dentro do dicionario
resultado = "email" in document
#print(resultado)
# del ~ passa como parametro o objeto q quer remover
#se não passar o parâmetro apagará o dicionario inteiro
del document["email"]
print(document)