import os
import time

def dados_conta():
    return {
        "saque_diario": 1,
        "SAQUE_MAXIMO": 500.00,
        "saldo": 0.0,
        "extrato": []
    }

def opcoes():
    os.system("cls")
    print(f"""
{"BANCO DO THEUZ".center(50, "=")}

[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

{"".center(50,"=")}
          """)
    
    opcao_escolhida = int(input())

    if 1 <= opcao_escolhida <= 4 :
        os.system("cls")
        return opcao_escolhida
    
    
    return input("\nDigite uma opção válida.\nPrecione a tecla ""Enter"" para continuar")

def deposito(conta):
    valor = float(input("\nInsira o valor que deseja depositar: "))
    
    if valor <= 0:
        return input("\nNão foi possível realizar o depósito. Por favor insira um valor positivo.\nPrecione a tecla ""Enter"" para continuar")
    
    conta["extrato"].append(f"Depósito R$ {valor:.2f}")
    conta["saldo"] += valor
    return input(f"O depósito no valor de R$ {valor:.2f} foi realizado com sucesso!\nPrecione a tecla ""Enter"" para continuar")
    
def saque(conta):
    valor = float(input("\nInsira o valor que deseja sacar: "))

    if valor <= 0:
        return input("\nNão foi possível realizar o saque. Por favor insira um valor positivo.\nPrecione a tecla ""Enter"" para continuar")
    elif valor > conta["SAQUE_MAXIMO"]:
        return input(f"\nNão foi possível realizar o saque. Você inseriu um valor maior que o limite de R$ {conta["SAQUE_MAXIMO"]:.2f} por saque.\nPrecione a tecla ""Enter"" para continuar")
    elif valor > conta["saldo"]:
        return input("\nNão foi possível realizar o saque por falta de saldo.\nPrecione a tecla ""Enter"" para continuar")
    elif conta["saque_diario"] > 3:
        return input("\nNão foi possível realizar o saque. Você atingiu o limite máximo de saque diário. Tente novamente amanhã!\nPrecione a tecla ""Enter"" para continuar")
    
    conta["saldo"] -= valor
    conta["extrato"].append(f"Saque R$ {valor:.2f}")
    conta["saque_diario"] += 1

    return input(f"O saque no valor de R$ {valor} foi realizado com sucesso!\nPrecione a tecla ""Enter"" para continuar")

def extrato(conta):
    for dado in conta["extrato"]:
        print(dado)
    input(f"\nSaldo atual da conta: R$ {conta["saldo"]:.2f}.\nPrecione a tecla ""Enter"" para continuar")

def sistema_bancario():
    conta = dados_conta()

    while True:
        opcao = opcoes()

        if opcao == 1:
            deposito(conta)
        if opcao == 2:
            saque(conta)
        if opcao == 3:
            extrato(conta)
        if opcao == 4:
            print("Obrigado!\nVolte Sempre.")
            time.sleep(3)
            break
            

def main():
    sistema_bancario()
    
if __name__ == "__main__":
    main()