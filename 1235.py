def decifrador(frase):
    frase = list(frase)
    frase_decifrada = []
    for i in range(((len(frase)// 2)-1), -1, -1):
        frase_decifrada.append(frase[i])
    for i in range((len(frase)-1), ((len(frase)// 2)-1), -1):
        frase_decifrada.append(frase[i])

    frase_final = "".join(frase_decifrada)
    print(frase_final)
    



def main():
    n = int(input())
    for i in range(n):
        frase = str(input())
        decifrador(frase)

main()
