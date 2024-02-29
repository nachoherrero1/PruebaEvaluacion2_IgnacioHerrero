class Galaxia:
    def __init__(self, nombre, tipo, estrellas=[]):
        self.nombre = nombre
        self.tipo = tipo
        self.estrellas = estrellas

    def __str__(self):
        return f"Galaxia: {self.nombre} ({self.tipo}) - Estrellas: {len(self.estrellas)}"

    def agregar_estrella(self, estrella):
        self.estrellas.append(estrella)

    def remover_estrella(self, estrella):
        self.estrellas.remove(estrella)
