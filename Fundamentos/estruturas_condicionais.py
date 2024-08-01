# MAIOR_IDADE = 18
# idade = 0

# while (idade !=99):
#     idade = int(input("Informe sua idade"))
#     if (idade>= MAIOR_IDADE):
#         print('Pode tirar CNH')
#     else:
#         print('Não pode tirar CNH')

conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 200
cheque_especial = 450
#estrutura ternária, primeiro a ação se for verdadeiro, segundo se não
status = "Sucesso" if saldo>= saque else "Falha"

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso')
        print(f"{status}")
    elif saque<=(saldo+cheque_especial):
        print("Saque permitido mediante uso do Chque Especial")
    else:
        print("Não ofi possível realiza o saque, saldo indisponível")
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso')
    elif saque<=(saldo+cheque_especial):
        print("Saque permitido mediante uso do Chque Especial")
    else:
        print("Não ofi possível realiza o saque, saldo indisponível")
else:
    print("Tipo de conta não identificado")