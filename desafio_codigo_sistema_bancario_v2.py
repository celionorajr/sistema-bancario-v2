menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar Usuário
[a] Abrir Conta
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []  # Lista para armazenar usuários
contas = []  # Lista para armazenar contas
numero_conta = 1  # Contador de contas

# Função para criar usuário
def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Usuário já cadastrado.")
        return
    
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    endereco = input("Endereço (logradouro - número - bairro - cidade/UF): ")
    usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")

# Função para criar conta
def criar_conta():
    global numero_conta
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if not usuario:
        print("Usuário não encontrado.")
        return
    
    contas.append({"agencia": "0001", "numero": numero_conta, "usuario": usuario})
    print(f"Conta {numero_conta} criada com sucesso para {usuario['nome']}!")
    numero_conta += 1

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
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
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor inválido para saque.")

    elif opcao == "e":
        print("\n=== Extrato Bancário ===")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=======================\n")
    
    elif opcao == "c":
        criar_usuario()
    
    elif opcao == "a":
        criar_conta()
    
    elif opcao == "q":
        print("Saindo do sistema bancário. Até mais!")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
