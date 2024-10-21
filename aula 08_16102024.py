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
        peso = float(input("Digite o peso dos peixes (em quilos): "))
multa = calcular_multa(peso)
if multa > 0:
    print(f"Você deve pagar uma multa de R$ {multa:.2f}.")
else:
    print("Você não precisa pagar multa.")
    def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"
        n = int(input("Quantas pessoas deseja avaliar? "))
for _ in range(n):
    peso = float(input("Digite o peso (em kg): "))
    altura = float(input("Digite a altura (em metros): "))
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    print(f"IMC: {imc:.2f} - Classificação: {classificacao}")
    def mostrar_cardapio():
    cardapio = {
        1: ("Hambúrguer", 19.00),
        2: ("Pizza", 35.00),
        3: ("Salada", 20.00),
        4: ("Refrigerante", 10.00),

           print("Cardápio:")
    for chave, (item, preco) in cardapio.items():
        print(f"{chave}. {item} - R$ {preco:.2f}")
    return cardapio

def realizar_pedido(cardapio):
    total = 0
    while True:
        pedido = int(input("Digite o número do item que deseja pedir (0 para finalizar): "))
        if pedido == 0:
            break
        elif pedido in cardapio:
            total += cardapio[pedido][1]
            print(f"Você adicionou {cardapio[pedido][0]} ao seu pedido.")
        else:
            print("Item inválido. Tente novamente.")

cardapio = mostrar_cardapio()
total = realizar_pedido(cardapio)
print(f"Total da conta: R$ {total:.2f}")
