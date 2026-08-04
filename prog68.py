class biscoito():
    def __init__(self,sabor,gosto):

        self.sabor = sabor
        self.gosto = gosto

    def croc(self):
        return f" {self.sabor} faz croc croc"

biscoito1 = biscoito("Chocolate", "forte")
biscoito2 = biscoito("Mel", "aconchegante")

print(f' Seu biscoito tem sabor de {biscoito1.sabor} e um gosto {biscoito1.gosto}')
print(f' Seu biscoito tem sabor de {biscoito2.sabor} e um gosto {biscoito2.gosto}')
print(biscoito1.croc())