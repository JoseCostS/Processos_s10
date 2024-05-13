class Veiculo:
    def acelerar(self):
        raise NotImplementedError("Método acelerar deve ser implementado.")

class Carro(Veiculo):
    def acelerar(self):
        print("Carro acelerando.")

class Motocicleta(Veiculo):
    def acelerar(self):
        print("Motocicleta acelerando.")

def acelerando():
   
    carro = Carro()
    motocicleta = Motocicleta()

    # Chamando o método acelerar de cada instância
    carro.acelerar()
    motocicleta.acelerar()

if __name__ == "adas":
    acelerando()


