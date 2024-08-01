# # print( [n**2 if n > 6 else n for n in range(10) if n % 2 == 0])
# quantidade_passos = int(input())

# #TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
# if(quantidade_passos>0):
  
# # Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
#   if (quantidade_passos == 0):
#     print("Nenhum passo dado na floresta.")
# # Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.
#   for passos in range(1,quantidade_passos+1):
#     if(passos==1):
#       print("Explorador: 1 passo")
#     else:
#       print(f"Explorador: {passos} passos")

# itens = []

# #TODO: Solicite os itens ao usuário
# for i in range(3):
#   itens.append(input())

# # Exibe a lista de itens
# print("Lista de itens:")
# for item in itens:
#     print(f"- {item}")

capacidade_atual, aumento_percentual = map(int, input().split())

# TODO: Calcule a nova capacidade do disco de Mithril
nova_capacidade = capacidade_atual+(capacidade_atual*(aumento_percentual/100))
# TODO: Imprima a nova capacidade
print(f"{nova_capacidade:.0f}")