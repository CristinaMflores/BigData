# 1) Um pescador precisa pagar uma multa caso o peso dos peixes exceda 100 quilos. Crie uma função para calcular a multa, se aplicável.
#
# 2) Crie um programa que faça a leitura da altura e do peso de N pessoas para o cálculo do IMC, mostrando ao final a classificação de acordo
# com a tabela de IMC.
#
# 3) Crie funções que mostrem um cardápio de um restaurante (pelo menos 4 itens) e que permitam realizar pedidos e fechar a conta.
#

def calcular_multa(peso_peixes):
    limite = 100
    multa_por_quilo = 4  # Exemplo de valor da multa por quilo excedido
    
    if peso_peixes > limite:
        excesso = peso_peixes - limite
        multa = excesso * multa_por_quilo
        return multa
    else:
        return 0
