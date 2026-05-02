class calculadora: 
    def __init__(self, x,y):
        self.x = x
        self.y = y 
    def soma(self):
        return self.x + self.y
    def subtracao(self):
        return self.x - self.y
if __name__ == "__main__":
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    calc = calculadora(x, y)
    print("A soma é:", calc.soma())
    print("A subtração é:", calc.subtracao())
    