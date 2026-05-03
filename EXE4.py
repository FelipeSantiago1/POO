class Pessoa:
    def __init__(self, nome, idade,peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def crescer(self):
        self.altura += 0.5
    def engordar(self,aumentoPeso):
        self.peso += aumentoPeso
        return self.peso
    def emagrecer(self, perdaPeso):
        self.peso -= 1
    def envelhecer(self):
        self.peso -= 1
if __name__ == "__main__":

    nome = input("Digite o nome da pessoa. ")
    idade = int(input("Digite a idade da pessoa. "))
    peso = float(input("Digite o peso da pessoa. "))
    altura = float(input("Digite a altura da pessoa." ))
    pessoa = Pessoa(nome,idade,peso,altura)
    print("Pessoa cadastrada")
    op = input("Deseja realizar algumas das operações a seguir \n Digite 1 para informar aumento  de peso \n Digite 2 para informar perda de peso \n Digite 3 para informar crescimento \n Digite 4 para informar envelhecimento")
    if op == "1":
        aumentoPeso = float(input("Digite o peso adicional (ganhado por você)"))
        pessoa.engordar(aumentoPeso)
        print(f"Peso atualizado: {pessoa.peso}")
    if op == "2":
        perdaPeso = float(input("Digite o peso a ser perdido: "))
        pessoa.emagrecer(perdaPeso)
        print(f"Peso atualizado: {pessoa.peso}")
    if op == "3":       
        pessoa.crescer()
        print(f"Altura atualizada: {pessoa.altura}")    
    
    
        
