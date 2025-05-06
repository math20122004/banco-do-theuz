import os
import time

def verificar_cpf(*, clientes, cpf):
    if cpf in clientes:
        return True
    return False

def criar_conta(*, clientes, contas):
    cpf =  str(input("Digite o CPF do titular: ")).strip()

    if verificar_cpf(clientes=clientes, cpf=cpf) == False:
        input("Cliente não encontrado.\nPor gentileza, cadastre o cliente para prosseguir.")
        return contas
    
    AGENCIA = "0001"
    
    numero_conta = len(contas) + 1
    conta_nova = {"saldo": 0, "AGENCIA": AGENCIA, "LIMITE_SAQUES": 3, "numeros saques": 0, "LIMITE": 500, "conta": numero_conta, "titular": clientes[cpf], "extrato": []}
    contas.append(conta_nova)

    clientes[cpf]["contas"].append(conta_nova)
    
    input(f"\nConta criada com sucesso!\nNúmero da conta: {numero_conta}\nPressione Enter para continuar.")
    return contas

def criar_cliente(clientes):
    cpf = str(input("Digite o seu CPF: "))

    if verificar_cpf(clientes=clientes, cpf=cpf):
        input("\nUsuário já cadastrado.\nPressione a tecla ""Enter"" para continuar...")
    else:
        nome = str(input("Digite o seu nome: "))
        data_nascimento = str(input("Digite a sua data de nascimento: "))
        
        logadouro = str(input("Digite o logradouro: "))
        numero = str(input("Digite o número: "))
        bairro = str(input("Digite o bairro: "))
        cidade = str(input("Digite a sua cidade: "))

        estados_validos = {
        "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
        "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
        "RS", "RO", "RR", "SC", "SP", "SE", "TO"
    }
        while True:
            estado = input("Digite a sigla do seu estado (ex: SP): ").strip().upper()

            if estado in estados_validos:
                break
            else:
                print("Sigla inválida! Tente novamente.")

        
        # endereco_completo = logadouro.rstrip() + " - " + numero.rstrip() + ", " + bairro.rstrip() + ". " + cidade.rstrip() + "/" + estado.strip()
        clientes[cpf] = {"nome": nome, "data de nascimento": data_nascimento, "endereco completo": {"logradouro": logadouro, "bairro": bairro, "numero": numero, "cidade": cidade, "estado": estado}, "contas": []}
    return clientes

def mostrar_contas(clientes, cpf):
    contas = clientes[cpf]["contas"]
    
    if not contas:
        print("Nenhuma conta cadastrada para este cliente.")
        return

    print(f"\nContas do cliente {clientes[cpf]['nome']}:\n")
    for conta in contas:
        print(f"Agência: {conta['AGENCIA']} | Conta: {conta['conta']}")
    
    input("\nPressione ""ENTER"" para continuar...")


def opcoes_conta():
    os.system("cls")
    print(f"""
{"BANCO DO THEUZ".center(50, "=")}

[0] Depósito
[1] Saque
[2] Extrato
[3] Listar Contas
[4] Voltar

{"".center(50,"=")}
          """)
    
    opcao_escolhida = int(input())

    if 0 <= opcao_escolhida <= 4:
        os.system("cls")
        return opcao_escolhida
    
    return input("\nDigite uma opção válida.\nPressione a tecla ""Enter"" para continuar")

def opcoes_primaria():
    os.system("cls")
    print(f"""
{"BANCO DO THEUZ".center(50, "=")}

[0] Criar Cliente
[1] Criar Conta
[2] Entrar na Conta
[3] Sair

{"".center(50,"=")}
          """)
    
    opcao_escolhida = int(input())

    if 0 <= opcao_escolhida <= 3 :
        os.system("cls")
        return opcao_escolhida
    
    return input("\nDigite uma opção válida.\nPressione a tecla ""Enter"" para continuar")


def escolher_contas(cpf, clientes):
    contas = clientes[cpf]["contas"]

    for conta in contas:
        print(f"Agência: {conta['AGENCIA']} | Conta: {conta['conta']} | Saldo: {conta['saldo']}")

    conta_deposito = input("Digite o número da conta em que deseja realizar a operação: ").strip()
    conta_selecionada = None

    for conta in contas:
        if str(conta["conta"]) == conta_deposito:
            conta_selecionada = conta
            break

    if not conta_selecionada:
        input("Número de conta não encontrado para este CPF. Pressione ENTER para continuar...")
        return
        
    return conta_selecionada
    
    

def sacar(*, conta_selecionada):
    while True:
        valor = float(input("\nInsira o valor que deseja sacar: "))

        if valor <= 0:
            input("\nNão foi possível realizar o saque. Por favor insira um valor positivo.\nPressione a tecla ""Enter"" para continuar")
        elif valor > conta_selecionada["LIMITE"]:
            input(f"\nNão foi possível realizar o saque. Você inseriu um valor maior que o limite de R$ {conta_selecionada["LIMITE"]:.2f} por saque.\nPressione a tecla ""Enter"" para continuar")
        elif valor > conta_selecionada["saldo"]:
            input("\nNão foi possível realizar o saque por falta de saldo.\nPressione a tecla ""Enter"" para continuar")
        elif conta_selecionada["numeros saques"] >= conta_selecionada["LIMITE_SAQUES"]:
            input("\nNão foi possível realizar o saque. Você atingiu o limite máximo de saque diário. Tente novamente amanhã!\nPressione a tecla ""Enter"" para continuar")
        else:
            conta_selecionada["saldo"] -= valor
            conta_selecionada["extrato"].append(f"Saque R$ {valor:.2f}")
            input(f"O saque no valor de R$ {valor:.2f} foi realizado com sucesso!\nPressione a tecla ""Enter"" para continuar")
            break

def depositar(conta_selecionada, /):
    while True:
        valor = float(input("\nInsira o valor que deseja depositar: "))
        
        if valor <= 0:
            input("\nNão foi possível realizar o depósito. Por favor insira um valor positivo.\nPressione a tecla ""Enter"" para continuar")
        else:
            conta_selecionada["saldo"] += valor
            conta_selecionada["extrato"].append(f"Depósito R$ {valor:.2f}")
            input(f"O depósito no valor de R$ {valor:.2f} foi realizado com sucesso!\nPressione a tecla ""Enter"" para continuar")
            break

def extrato_conta(conta_selecionada):
    for extrato in conta_selecionada["extrato"]:
        print(extrato)
    input(f"\nSaldo atual da conta: R$ {conta_selecionada["saldo"]}.\nPressione a tecla ""Enter"" para continuar")

def main():
    extrato = []
    clientes = {}
    contas = []

    while True:
        opcao = opcoes_primaria()

        if opcao == 0:
            clientes = criar_cliente(clientes)
        if opcao == 1:
            contas = criar_conta(clientes=clientes, contas=contas)
        if opcao == 2:
            cpf = str(input("Digite o CPF do titular: "))
            if verificar_cpf(clientes=clientes, cpf=cpf) == False:
                print("CPF não encontrado.\nCadastre um usuário")
                time.sleep(3)
            else:
                conta_selecionada = escolher_contas(cpf, clientes)
                while True:   
                    opcao_dois = opcoes_conta()

                    if opcao_dois == 0:
                        depositar(conta_selecionada)
                    if opcao_dois == 1:
                        sacar(conta_selecionada=conta_selecionada)
                    if opcao_dois == 2:
                        extrato_conta(conta_selecionada)
                    if opcao_dois == 3: 
                        mostrar_contas(clientes, cpf)
                    if opcao_dois == 4:
                        break
        if opcao == 3:
            print("Obrigado!\nVolte Sempre.")
            time.sleep(3)
            break
    
if __name__ == "__main__":
    main()
