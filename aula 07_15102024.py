# Crie um código que seja capaz de ler e armazenar
# uma sequência de 20 números pares e 20 números ímpares.
# Obs: utilize estruturas de repetição para fechar esse conjunto
# de números.

numeros_pares = []
numeros_impares = []

while len(numeros_pares) < 20 or len(numeros_impares) < 20:
     numero = int(input("Digite um número: "))
  if len(numeros_pares) < 20:
            numeros_pares.append(numero)
            print(f"Número par adicionado: {numero}")
        else:
            print("Já foram adicionados 20 números pares.")
    else:
        if len(numeros_impares) < 20:
            numeros_impares.append(numero)
            print(f"Número ímpar adicionado: {numero}")
        else:
            print("Já foram adicionados 20 números ímpares.")
