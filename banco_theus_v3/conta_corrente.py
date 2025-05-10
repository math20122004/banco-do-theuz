from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, cliente):
        self._limite = 500
        self._limite_transacoes = 3
        super().__init__(cliente)

    def sacar(self, valor):
        if valor > self._limite:
            input(f"\nNão foi possível realizar o saque. Você inseriu um valor maior que o limite de R$ {self.limite:.2f} por saque.\nPressione a tecla ""Enter"" para continuar")
            return False
        elif self._limite_transacoes == 0:
            input("\nNão foi possível realizar o saque. Você atingiu o limite máximo de transações diário. Tente novamente amanhã!\nPressione a tecla ""Enter"" para continuar")
            return False
        else:
            self._limite_transacoes -= 1
            return super().sacar(valor)
        
    