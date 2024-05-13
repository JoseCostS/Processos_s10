class Lampada:
    def __init__(self):
        self.estado = False  # Começa desligada

    def alterar_estado(self):
        self.estado=not self.estado
        return"ligado"if self.estado else"desligado"
    
# Uso da classe
lampada = Lampada()
print(lampada.alterar_estado())  # Liga a lâmpada

print(lampada.alterar_estado())  # Desliga a lâmpada


