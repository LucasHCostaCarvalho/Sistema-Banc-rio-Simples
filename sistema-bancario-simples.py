menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIO = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 2:
        if numero_saques >= LIMITE_SAQUES_DIARIO:
            print("Operação falhou! Número máximo de saques excedido.")
            continue

        if saldo == 0:
            print("Operação falhou! Atualmente você não possue saldo em sua conta.")
            continue
        else:
            print(f"Seu saldo atual é de {saldo:.2f}")

        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_saque            

        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite de saque. Valor maximo é de R$ 500.00")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == 4:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
