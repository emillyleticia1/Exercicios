#Exercio 1:

class Veiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def frear(self):
        return f"Carro de marca {self.marca} de modelo {self.modelo} está freiando"

    def acelerar(self):
        return f"Carro de marca {self.marca} de modelo {self.modelo}  está acelerando"

class Carro(Veiculo):
    def __init__(self,marca,modelo,cor):
        super().__init__(marca,modelo)
        self.cor = cor

    def Abrir_Porta(self):
        print("Porta aberta")

class Moto(Veiculo):
    def _init_(self, marca, cor, cilindada, enpinar):
        super()._init_(marca)
        self.cor = cor
        self.cilindada = cilindada
        self.enpinar = enpinar

    def empinar(self, vezes):
        print(f"A moto da marca {self.marca} empinou {vezes} vezes!")

if _name=="main_":
 marca = input("Insira a marca da moto: ")
 cor = input("Insira a cor da moto: ")
 cilindada = input("Insira a cilindrada da moto: ")
 enpinar = input("Insira a capacidade de empinar da moto: ")
 vezes_empinar = int(input("Quantas vezes a moto irá empinar? "))
moto1 = Moto(marca=marca, cor=cor, cilindada=cilindada, enpinar=enpinar)
moto1.empinar(vezes_empinar)







