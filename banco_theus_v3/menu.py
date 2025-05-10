import os
from conta_corrente import ContaCorrente
from pessoa_fisica import PessoaFisica

class Menu:
    @classmethod
    def opcoes_primaria(cls):
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

    

    @classmethod
    def escolher_contas(cls, cliente):
        Menu.mostrar_contas(cliente)

        if not cliente.contas:
            return

        conta_deposito = input("Digite o número da conta em que deseja realizar a operação: ").strip()
        conta_selecionada = None

        for conta in cliente.contas:
            if str(conta.numero) == conta_deposito:
                conta_selecionada = conta
                break

        if not conta_selecionada:
            input("Número de conta não encontrado para este CPF. Pressione ENTER para continuar...")
            return
            
        return conta_selecionada
