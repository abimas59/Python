# texto = input("Informe um texto: ")
# VOGAIS = "AEIOU"

# for letra in texto: #string é um objeto em python
#     if letra.upper() in VOGAIS:
#         print(letra, end="")
# else:#executa ao terminar
#     print()
#     print("Ao terminar")

#######################################################
#for numero in range (start, stop, step) 
#
numero = int(input("Digite um número"))
print(f"TABUADA DE {numero}: ")
for i in range (0,11):
    #print(i, end="")
    print(i," X ",numero," = ",(numero*i),end="\n")

#
#while opcao != 0:
#   logica
#   break;
#continua pula oq iria acontecer em seguida
#else: