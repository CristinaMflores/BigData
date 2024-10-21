#Leia três pares de números inteiros fornecidos pelo usuário, calcule e imprima a soma de cada par separadamente. Utilize 
#tratamento de erros para garantir que os valores inseridos sejam válidos e, se o número for ÍMPAR, ter uma exceção personalizada.

numeros_pares = []
numeros_impares = []

while len(numeros_pares) < 20 or len(numeros_impares) < 20:
  
  numero = int(input("Digite um número: "))
  if len(numeros_pares) < 20:

   
