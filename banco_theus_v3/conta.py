import random
from historico import Historico

class Conta:
    def __init__(self, cliente):
        self._saldo = 0
        self._numero = random.randint(0, 100)
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente):
        return cls(cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @property
    def limite(self):
        return self._limite
    
    @property
    def limite_transacoes(self):
        return self._limite_transacoes
    
    def sacar(self, valor):
        if valor <= 0:
            input("\nNão foi possível realizar o saque. Por favor insira um valor positivo.\nPressione a tecla ""Enter"" para continuar")
            return False
        elif valor > self._saldo:
            input("\nNão foi possível realizar o saque por falta de saldo.\nPressione a tecla ""Enter"" para continuar")
            return False
        else:
            self._saldo -= valor
            input(f"O saque no valor de R$ {valor:.2f} foi realizado com sucesso!\nPressione a tecla ""Enter"" para continuar")
            return True
        
    def depositar(self, valor):
        if valor <= 0:
            input("\nNão foi possível realizar o depósito. Por favor insira um valor positivo.\nPressione a tecla ""Enter"" para continuar")
            return False
        elif self._limite_transacoes == 0:
            input("\nNão foi possível realizar o depósito. Você atingiu o limite máximo de transações diário. Tente novamente amanhã!\nPressione a tecla ""Enter"" para continuar")
            return False       
        else:
            self._saldo += valor
            self._limite_transacoes -= 1
            input(f"O depósito no valor de R$ {valor:.2f} foi realizado com sucesso!\nPressione a tecla ""Enter"" para continuar")
            return True



    
