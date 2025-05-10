import time
from menu import Menu
from operacoes_menu import Operacoes

class Main:
    clientes = []

    while True:
        opcao = Menu.opcoes_primaria()

        if opcao == 0:
            Operacoes.criar_cliente(clientes)
        if opcao == 1:
            Operacoes.criar_conta(clientes)
        if opcao == 2:
            cpf = Operacoes.validar_cpf(clientes)
            if cpf is None:
                break
            conta = Operacoes.escolher_conta(clientes, cpf)
            if conta is None:
                pass
            else:
                while True:   
                    opcao_dois = Menu.opcoes_conta()

                    if opcao_dois == 0:
                        Operacoes.depositar(clientes, cpf, conta)
                    if opcao_dois == 1:
                        Operacoes.sacar(clientes, cpf, conta)
                    if opcao_dois == 2:
                        Operacoes.exibir_extrato(clientes, cpf, conta)
                    if opcao_dois == 3: 
                        Operacoes.mostrar_contas(clientes, cpf)
                    if opcao_dois == 4:
                        break
        if opcao == 3:
            print("Obrigado!\nVolte Sempre.")
            time.sleep(3)
            break

if __name__ == "__main__":
    Main()