def ascii(numero_textos):
    for i in range(numero_textos):
        texto = list(input())

        for letra in range(len(texto)):
            codigo = ord(texto[letra])
            if codigo >= 65 and codigo <= 126:
                codigo = (codigo +3)
                texto[letra] = chr(codigo)
            else:
                texto[letra] = texto[letra]

        inversor(texto)

def inversor(texto):
    texto_invertido = []
    for i in range(len(texto)):
        texto_invertido.insert(0, texto[i])
    ascii2(texto_invertido)

def ascii2(texto_invertido):
    for i in range((len(texto_invertido)), ((len(texto_invertido) // 2)), -1):
        codigo = ord(texto_invertido[i-1])
        codigo = codigo - 1
        texto_invertido[i-1] = chr(codigo)
    texto_final = "".join(texto_invertido)
    print(texto_final)



def main():
    numero_textos = int(input())
    ascii(numero_textos)

main()
