if __name__ == "__main__":
    generar_galaxia()

from Estrella import Estrella

# Creación de estrellas
estrella_a = Estrella(2, 3, 1)
estrella_b = Estrella(4, 4, 4)
estrella_c = Estrella(-3, -1, 0)

# Imprimir información
print(f"**Estrellas:**")
print(estrella_a)
print(estrella_b)
print(estrella_c)

# Galaxias
print("\n**Galaxias:**")
print(f"Estrella A ({estrella_a.x:.2f}, {estrella_a.y:.2f}, {estrella_a.z:.2f}) está en la {estrella_a.galaxia()}")
print(f"Estrella B ({estrella_b.x:.2f}, {estrella_b.y:.2f}, {estrella_b.z:.2f}) está en la {estrella_b.galaxia()}")
print(f"Estrella C ({estrella_c.x:.2f}, {estrella_c.y:.2f}, {estrella_c.z:.2f}) está en la {estrella_c.galaxia()}")

# Distancias
print("\n**Distancias:**")
distancia_ab = estrella_a.distancia(estrella_b)
distancia_bc = estrella_b.distancia(estrella_c)

print(f"Distancia entre A y B: {distancia_ab:.2f}")
print(f"Distancia entre B y C: {distancia_bc:.2f}")

# Estrella más lejos del origen
print("\n**Estrella más lejos del origen:**")
estrella_mas_lejana = max([estrella_a, estrella_b, estrella_c], key=lambda e: e.distancia((0, 0, 0)))
print(f"Estrella más lejos del origen: {estrella_mas_lejana}")
