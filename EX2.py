class Bola: 
    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material
    def mostrarCor(self):
        return self.cor
    def trocarCor(self, nova_cor):
        self.cor = nova_cor

if __name__ == "__main__":
    cor = input("Digite a cor da bola: ")
    circuferencia = float(input("Digite a circunferência da bola: "))
    material = input("digite o material da bola:")
    bola = Bola(cor, circuferencia, material)
    print("A cor da bola é:", bola.mostrarCor())
    if input("Deseja trocar a cor da bola? (s/n): ").lower() == 's':
        nova_cor = input("Digite a nova cor da bola: ")
        bola.trocarCor(nova_cor)
        print("A nova cor da bola é:", bola.mostrarCor())
