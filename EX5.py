class ContaCorrente:
    def __init__(self,numConta,nomeCorrentista):
        self.numConta = numConta
        self.nomeCorrentista= nomeCorrentista
        self.saldo = 500
    def alterarNome(self, nomeNovo):
        self.nomeCorrentista = nomeNovo
    def deposito(self, deposito):
        self.saldo += deposito
    def saque(self, valorSaque):
        self.saldo -= valorSaque
    def mostrarSaldo(self):
        return (self.saldo)
if __name__ == "__main__":

    numConta = int(input("Digite o numero da conta. \n "))
    nomeCorrentista = input("Digite o nome do correntista. \n ")
    
    contaCorrente = ContaCorrente(numConta,nomeCorrentista)

    op = int(input("Deseja fazer um saque ? digite 1. \n Deseja fazer um deposito digite 2 \n Deseja alterar o nome do correntista digite 3 \n Deseja mostrar o saldo digite 4 \n "))
    if op == 1:
        valorSaque = float(input(f"Digite o valor do saque que deseja \n\n valor disponível para saque é{contaCorrente.mostrarSaldo()} \n "))
        contaCorrente.saque(valorSaque)
        print(f" Valor sacado: {valorSaque} \n Valor disponível (saldo atualizado){contaCorrente.mostrarSaldo()}\n ")

    if op == 2:
        deposito = float(input(f"Digite o valor do deposito que deseja \n\n valor disponível para deposito é{contaCorrente.mostrarSaldo()}\n "))
        contaCorrente.deposito(deposito)
        print(f" Valor depositado: {deposito} \n Valor disponível (saldo atualizado){contaCorrente.mostrarSaldo()}\n ")
    if op == 3:
        nomeNovo = input("Digite o novo nome do correntista. \n ")
        contaCorrente.alterarNome(nomeNovo)
        print(f" Nome atualizado: {contaCorrente.nomeCorrentista} \n ")            
    if op == 4:
        print(f" Saldo disponível: {contaCorrente.mostrarSaldo()} \n ")
    
