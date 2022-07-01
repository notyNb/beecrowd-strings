def combinador(linha1):
    linha1 = list(linha1)
    linha1_1 = []
    linha_final = []
    soma = 0
    for i in range(len(linha1)):
        code = ord(linha1[0])
        if code != 32:
            linha1_1.append(linha1[0])
            soma += 1
            del linha1[0]
        elif code == 32:
            del linha1[0]
            break
    if soma > (len(linha1)):

        for i in range(len(linha1)):
            linha_final.append(linha1_1[0])
            linha_final.append(linha1[i])
            del linha1_1[0]
    
        for i in range(len(linha1_1)):
            linha_final.append(linha1_1[i])
    
        final = "".join(linha_final)
        print(final)


    else:    
    #if 2 maior
        for i in range(len(linha1_1)):
            linha_final.append(linha1_1[i])
            linha_final.append(linha1[0])
            del linha1[0]
    
        for i in range(len(linha1)):
            linha_final.append(linha1[i])
    
        final = "".join(linha_final)
        print(final)
    
    


def main():
    while True:
        try:
            n = int(input())
            for i in range(n):
                linha1 = input()
                combinador(linha1)
        except EOFError:
            break
        
           
        
main()
