from datetime import datetime

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
numero_transacoes = 0
LIMITE_SAQUES = 3
LIMITE_TRANSACOES = 10

while True:
    opcao = input(menu)

    if opcao in ["d", "s"] and numero_transacoes >= LIMITE_TRANSACOES:
        print("Limite diário de transações atingido.")
        continue

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Depósito: R$ {valor:.2f}")
            numero_transacoes += 1
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diários atingido.")
        elif valor > limite:
            print("Valor de saque excede o limite permitido.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        elif valor > 0:
            saldo -= valor
            extrato.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Saque: R$ {valor:.2f}")
            numero_saques += 1
            numero_transacoes += 1
        else:
            print("Valor inválido para saque.")

    elif opcao == "e":
        print("\n=== Extrato Bancário ===")
        print("\n".join(extrato) if extrato else "Não foram realizadas movimentações.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=======================\n")

    elif opcao == "q":
        print("Saindo do sistema bancário. Até mais!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
