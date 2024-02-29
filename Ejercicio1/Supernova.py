from Estrella import Estrella

class Supernova(Estrella):
    def __init__(self, x, y, z, brillo, temperatura, masa):
        super().__init__(x, y, z, brillo, temperatura)
        self.masa = masa

    def explotar(self):
        print(f"¡Supernova en ({self.x}, {self.y}, {self.z})!")

