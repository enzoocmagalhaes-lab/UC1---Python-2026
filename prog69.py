class passarinho():
    def __init__(self,raça,cor):
        self.raça = raça
        self.cor = cor

    def cantar(self):
        return f' onde a raça {self.raça} canta'

passarinho1 = passarinho('Canário', 'amarelo')
passarinho2 = passarinho('Cardeal', 'Vermelho')

print(f'O passarinho da raça {passarinho1.raça} é da cor {passarinho1.cor}')
print(f'O passarinho da raça {passarinho2.raça} é da cor {passarinho2.cor}')
print(passarinho1.cantar())