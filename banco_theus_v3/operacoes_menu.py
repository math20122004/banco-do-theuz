import time
from saque import Saque
from deposito import Deposito
from pessoa_fisica import PessoaFisica
from conta_corrente import ContaCorrente


class Operacoes:
    def criar_cliente(clientes):
        cpf = input("Digite seu CPF: ")
        nome = input("Digite seu nome: ")
        data_nascimento = input("Digite sua data de nascimento: ")
        endereco = input("Digite seu endereço: ")

        clientes.append(PessoaFisica(endereco, nome, cpf, data_nascimento))
        input("Cliente cadastrado com sucesso!\nPressione a tecla ""Enter"" para continuar")
    
    def criar_conta(clientes):
        cpf_cliente = input("Digite o CPF do titular: ").strip()

        for cliente in clientes:
            if cliente.cpf == cpf_cliente:
                conta = ContaCorrente(cliente)
                cliente.adicionar_conta(conta)
                print(f"Conta cadastrada com sucesso!\nNúmero da conta: {conta.numero}")
                input("Pressione a tecla ""Enter"" para continuar\n")
                return
        input("Cliente não encontrado para o CPF informado.\nPressione a tecla ""Enter"" para continuar")

    def escolher_conta(clientes, cpf):
        for cliente in clientes:
            if cliente.cpf == cpf:
                contas =  cliente.contas
                if not contas:
                    print("Nenhuma conta cadastrada para este cliente.")
                    return None
                
                for conta in contas:
                    print(f"Agência: {conta.agencia} | Conta: {conta.numero} | Saldo: {conta.saldo:.2f}")

                conta_selecionada = input("Digite o número da conta que deseja realizar a operação: ").strip()

                for conta in contas:
                    if str(conta.numero) == conta_selecionada:
                        return conta
                    
                input("Número de conta não encontrado para este CPF. Pressione ENTER para continuar...")
                return None
                
        input("CPF não encontrado. Pressione ENTER para continuar...")
        return None
                
    
    def mostrar_contas(clientes, cpf):
        for cliente in clientes:
            if cliente.cpf == cpf:
                contas =  cliente.contas
                if not contas:
                    print("Nenhuma conta cadastrada para este cliente.")
                    return
        
                print(f"\nContas do cliente {cliente.nome}:\n")
                for conta in contas:
                    print(f"Agência: {conta.agencia} | Conta: {conta.numero} | Saldo: {conta.saldo:.2f}")
                
                input("\nPressione ""ENTER"" para continuar...")
                return
        input("CPF não encontrado. Pressione ENTER para continuar...")
        return 

    def validar_cpf(clientes):
        cpf = str(input("Digite o CPF do titular: "))
        for cliente in clientes:
            if cliente.cpf == cpf:
                return cpf
            
        print("CPF não encontrado.\nCadastre um usuário.")
        time.sleep(3)
        return None
    
    def sacar(clientes, cpf, conta):
        for cliente in clientes:
            if cliente.cpf == cpf:
                for conta_cliente in cliente.contas:
                    if conta_cliente.numero == conta.numero:
                        valor = float(input("Digite o valor deseja sacar: "))
                        try:
                            s1 = Saque(valor)
                            s1.registrar(conta)
                            return
                        except ValueError:
                            input("Valor inválido. Por favor, digite um número.\nPressione ENTER para continuar...")
                            return
                        except Exception as e:
                            input(f"Erro ao realizar o saque: {e}\nPressione ENTER para continuar...")
                            return
        input("Conta ou cliente não encontrados.\nPressione ENTER para continuar...")

    def depositar(clientes, cpf, conta):
        for cliente in clientes:
            if cliente.cpf == cpf:
                for conta_cliente in cliente.contas:
                    if conta_cliente.numero == conta.numero:
                        valor = float(input("Digite o valor deseja depositar: "))
                        try:
                            d1 = Deposito(valor)
                            d1.registrar(conta)
                            return
                        except ValueError:
                            input("Valor inválido. Por favor, digite um número.\nPressione ENTER para continuar...")
                            return
                        except Exception as e:
                            input(f"Erro ao realizar o depósito: {e}\nPressione ENTER para continuar...")
                            return
        input("Conta ou cliente não encontrados.\nPressione ENTER para continuar...")

    def exibir_extrato(clientes, cpf, conta):
        for cliente in clientes:
            if cliente.cpf == cpf:
                for conta_cliente in cliente.contas:
                    if conta_cliente.numero == conta.numero:
                        
                        for transacao in conta.historico.transacoes:
                            print(f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}\n\t{transacao['data']}")

                        input("\nPressione ENTER para continuar...")