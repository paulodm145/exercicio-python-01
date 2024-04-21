# Variáveis globais
saldo = 0.0
transacoes = []
saques_diarios = 3

def depositar():
    global saldo, transacoes
    valor = float(input("Informe o valor a ser depositado: "))
    if valor > 0:
        saldo += valor
        transacoes.append(f"Depósito: R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        print("Depósito realizado com sucesso.")
    else:
        print("O valor do depósito deve ser positivo.")

def sacar():
    global saldo, transacoes, saques_diarios
    valor = float(input("Informe o valor a ser sacado: "))
    if valor > 500:
        print("O valor máximo por saque é de R$ 500,00.")
    elif saques_diarios >= 3:
        print("Limite diário de saques alcançado.")
    elif saldo >= valor:
        saldo -= valor
        saques_diarios += 1
        transacoes.append(f"Saque: R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        print("Saque realizado com sucesso.")
    else:
        print("Saldo insuficiente para realizar o saque.")

def extrato():
    global saldo, transacoes
    print("Extrato da conta:")
    for transacao in transacoes:
        print(transacao)
    print(f"Saldo Atual: R$ {saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

def main():
    while True:
        print("\nMenu de Opções:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            depositar()
        elif opcao == '2':
            sacar()
        elif opcao == '3':
            extrato()
        elif opcao == '4':
            print("Obrigado por usar nosso sistema bancário.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()