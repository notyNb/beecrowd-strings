def bloggo(t:str):
    t = list(t)
    italico = negrito = False
    for i in range(len(t)):
        if t[i] == "_":
            if not italico:
                t[i] = "<i>"
                italico = True
            else:
                t[i] = "</i>"
                italico = False
        elif t[i] == "*":
            if not negrito:
                t[i] = "<b>"
                negrito = True
            else:
                t[i] = "</b>"
                negrito = False
    
    return "".join(t)




def main():
    while True:
        try:
            t = input()
            print(bloggo(t))
        except EOFError:
            break
main()
