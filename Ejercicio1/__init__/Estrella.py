class Estrella:
    def __init__(self, x, y, z, brillo, temperatura):
        self.x = x
        self.y = y
        self.z = z
        self.brillo = brillo
        self.temperatura = temperatura

    def __str__(self):
        return f"Estrella: ({self.x}, {self.y}, {self.z}) - Brillo: {self.brillo}, Temperatura: {self.temperatura}"

    def distancia(self, otra_estrella):
        import math
        return math.sqrt((self.x - otra_estrella.x)**2 +
                        (self.y - otra_estrella.y)**2 +
                        (self.z - otra_estrella.z)**2)

