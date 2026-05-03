class Retangulo: 
    def __init__(self , base , altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
if __name__ == "__main__":
    base = float(input("Digite o valor correspondente a base do retângulo (comprimento)."))
    altura = float(input("Digite o valor correspondente a altura do retângulo."))
    retangulo = Retangulo(base, altura)
    print(f"A área do retângulo calculada é:{retangulo.area()}")
    
