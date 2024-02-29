from Estrella import Estrella

class EnanaRoja(Estrella):
    def __init__(self, x, y, z, brillo, temperatura, masa):
        super().__init__(x, y, z, brillo, temperatura)
        self.masa = masa

