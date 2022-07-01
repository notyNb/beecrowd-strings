def somatoria(valor: list, lista_led: list, lista_valoresLed: list):
    leds = 0
    a = 0
    for i in range(len(valor)):
        for j in range(len(lista_led)):
            
            if valor[i] == lista_led[j]:
                leds += lista_valoresLed[j]
                
            else:
                a += 1
    print(f"{leds} leds")






def main():
    casos_teste = int(input())
    lista_led = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    lista_valoresLed = [2, 5, 5, 4, 5, 6, 3, 7, 6, 6]
    for i in range(casos_teste):
        valor = list(map(int, input()))
        somatoria(valor, lista_led, lista_valoresLed)


main()
