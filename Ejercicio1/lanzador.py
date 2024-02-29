from Ejercicio1.EnanaRoja import EnanaRoja
from Ejercicio1.GiganteAzul import GiganteAzul
from Ejercicio1.Supernova import Supernova
from Ejercicio1.__init__ import Estrella
from Ejercicio1.__init__ import Galaxia

# Creación de estrellas
enana_roja = EnanaRoja(1, 2, 3, 10, 3000, 0.5)
gigante_azul = GiganteAzul(4, 5, 6, 100, 10000, 10)
supernova = Supernova(7, 8, 9, 1000, 20000, 20)

# Creación de galaxias
galaxia_a = Galaxia("Vía Láctea", "Espiral", [enana_roja, gigante_azul])
galaxia_b = Galaxia("Andrómeda", "Elíptica", [supernova])

# Agregar una estrella a una galaxia
galaxia_a.agregar_estrella(supernova)

# Imprimir información
print(enana_roja)
print(gigante_azul)
print(supernova)

print(galaxia_a)
print(galaxia_b)

# Simular explosión de supernova
supernova.explotar()

# Remover la supernova de la galaxia
galaxia_a.remover_estrella(supernova)

print(galaxia_a)
def main():
    # Creación de estrellas
    enana_roja = EnanaRoja(1, 2, 3, 10, 3000, 0.5)
    gigante_azul = GiganteAzul(4, 5, 6, 100, 10000, 10)
    supernova = Supernova(7, 8, 9, 1000, 20000, 20)

    # Creación de galaxias
    galaxia_a = Galaxia("Vía Láctea", "Espiral", [enana_roja, gigante_azul])
    galaxia_b = Galaxia("Andrómeda", "Elíptica", [supernova])

    # Agregar una estrella a una galaxia
    galaxia_a.agregar_estrella(supernova)

    # Imprimir información
    print(enana_roja)
    print(gigante_azul)
    print(supernova)

    print(galaxia_a)
    print(galaxia_b)

    # Simular explosión de supernova
    supernova.explotar()

    # Remover la supernova de la galaxia
    galaxia_a.remover_estrella(supernova)

    print(galaxia_a)

if __name__ == "__main__":
    main()