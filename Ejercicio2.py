class Dialogo:
    def __init__(self, texto):
        self.texto = texto

    def formatear_dialogo(self):
        partes = self.texto.split('#')
        return "\n\n".join(part.capitalize() + "." for part in partes)

texto_original = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

dialogo = Dialogo(texto_original)
texto_formateado = dialogo.formatear_dialogo()
print(texto_formateado)