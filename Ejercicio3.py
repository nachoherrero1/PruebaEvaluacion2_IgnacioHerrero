class MagiaNumerica:
    def __init__(self):
        self.lista_numeros = []

    def obtener_numeros(self):
        num = input("Introduce un número (o 'q' para terminar): ")
        while num != 'q':
            try:
                num = int(num)
                self.lista_numeros.append(num)
            except ValueError:
                print("Error: Introduce un número válido.")
            num = input("Introduce un número (o 'q' para terminar): ")

    def obtener_lista_final(self):
        lista_sin_duplicados = list(set(self.lista_numeros))
        lista_ordenada = sorted(lista_sin_duplicados, reverse=True)
        lista_sin_impares = [num for num in lista_ordenada if num % 2 == 0]
        suma = sum(lista_sin_impares)
        lista_final = [suma] + lista_sin_impares
        return lista_final

if __name__ == "__main__":
    magia = MagiaNumerica()
    magia.obtener_numeros()
    resultado = magia.obtener_lista_final()
    print(resultado)

    verificacion = resultado[0] == sum(resultado[1:])
    print(verificacion)
