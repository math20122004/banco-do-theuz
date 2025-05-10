from transacao import Transacao

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        super().__init__()

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self._valor)

        if sucesso_transacao:
            conta.historico.registrar_transacao(self)