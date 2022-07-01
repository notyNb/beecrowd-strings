def frequencia(t:str):
    cont = [0] * 26

    for letra in t:
        cod = ord(letra)
        if cod >= 97 and cod <= 122:
            cont[cod - 97] += 1
        elif cod >= 65 and cod <= 90:
            cont[cod - 65] += 1

    m = maior(cont)
    imprimir(cont, m)

#=========
def imprimir(cont:list, m: int):
    for i in range(len(cont)):
        if cont[i] == m:
            print(chr(i + 97), end="")
    
    print("")
#===========
def maior(x: list) -> int:
    maior = x[0]
    for i in range(1, len(x)):
        if x[i] > maior:
            maior = x[i]

    return maior
#==========

def main():
    n = int(input())

    for i in range(n):
        t = input()
        frequencia(t)

main()
