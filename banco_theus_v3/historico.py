from datetime import datetime

class Historico:
    def __init__(self):
        self._historico_transacoes = []

    @property
    def transacoes(self):
        return self._historico_transacoes
    
    def registrar_transacao(self, transacao):
        self._historico_transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }
        )