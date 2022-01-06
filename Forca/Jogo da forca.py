import random

with open('palavras.txt','r') as arquivo:
    texto = arquivo.readlines()

numero_ale = random.randint(0,((len(texto)-1)))

palavra = texto[numero_ale]

quantidade = 0
escondida = ((len(palavra)-1) * '_')
print('|''-''-''-''-')
print('|')
print('|')
print('|')
print('|')
print(escondida)

list_tentativa = []

while quantidade < 7:
    tentativa = input('Insira uma letra:\n')

    if tentativa in list_tentativa:
        print('Você já tentou esta letra!')
    if tentativa not in list_tentativa:
        list_tentativa.append(tentativa)
        print(f'Você tentou as seguintes letras: {list_tentativa}')
    if tentativa in palavra:
        posicao = palavra.find(tentativa)
        escondida = (escondida[0:posicao] + tentativa + escondida[(posicao+1):])
        posicao2 = palavra.find(tentativa, (posicao+1), (len(palavra)-1))
        if posicao2 > posicao:
            escondida = (escondida[0:posicao2] + tentativa + escondida[(posicao2 + 1):])
            posicao3 = palavra.find(tentativa, (posicao2 + 1), (len(palavra) - 1))
            if posicao3 > posicao2:
                escondida = (escondida[0:posicao3] + tentativa + escondida[(posicao3 + 1):])
        if quantidade == 0:
            print('|''-''-''-''-')
            print('|')
            print('|')
            print('|')
            print('|')
            print(escondida)
        elif quantidade == 1:
            print('|''-''-''-''-')
            print('|'' '' '' ''O')
            print('|')
            print('|')
            print('|')
            print(escondida)
        elif quantidade == 2:
            print('|''-''-''-''-')
            print('|'' '' '' ''O')
            print('|'' '' '' ''|')
            print('|')
            print('|')
            print(escondida)
        elif quantidade == 3:
            print('|''-''-''-''-')
            print('|'' '' '' ''O')
            print('|'' '' '' ''|')
            print('|'' '' '' ''/')
            print('|')
            print(escondida)
        elif quantidade == 4:
            print('|''-''-''-''-')
            print('|'' '' '' ''O')
            print('|'' '' '' ''|')
            print('|'' '' '' ''/\\')
            print('|')
            print(escondida)
        elif quantidade == 5:
            print('|''-''-''-''-')
            print('|'' '' '' ''O')
            print('|'' '' ''/|')
            print('|'' '' '' ''/\\')
            print('|')
            print(escondida)
        elif quantidade == 6:
            print('|''-''-''-''-')
            print('|'' '' '' ''O')
            print('|'' '' ''/|\\')
            print('|'' '' '' ''/\\')
            print('|')
            print(escondida)
    if tentativa not in palavra and quantidade == 0:
        print('Essa letra não existe.')
        print('|''-''-''-''-')
        print('|'' '' '' ''O')
        print('|')
        print('|')
        print('|')
        print(escondida)
        quantidade = 1
    elif tentativa not in palavra and quantidade == 1:
        print('Essa letra não existe.')
        print('|''-''-''-''-')
        print('|'' '' '' ''O')
        print('|'' '' '' ''|')
        print('|')
        print('|')
        print(escondida)
        quantidade = 2
    elif tentativa not in palavra and quantidade == 2:
        print('Essa letra não existe.')
        print('|''-''-''-''-')
        print('|'' '' '' ''O')
        print('|'' '' '' ''|')
        print('|'' '' '' ''/')
        print('|')
        print(escondida)
        quantidade = 3
    elif tentativa not in palavra and quantidade == 3:
        print('Essa letra não existe.')
        print('|''-''-''-''-')
        print('|'' '' '' ''O')
        print('|'' '' '' ''|')
        print('|'' '' '' ''/\\')
        print('|')
        print(escondida)
        quantidade = 4
    elif tentativa not in palavra and quantidade == 4:
        print('Essa letra não existe.')
        print('|''-''-''-''-')
        print('|'' '' '' ''O')
        print('|'' '' ''/|')
        print('|'' '' '' ''/\\')
        print('|')
        print(escondida)
        quantidade = 5
    elif tentativa not in palavra and quantidade == 5:
        print('Essa letra não existe.')
        print('|''-''-''-''-')
        print('|'' '' '' ''O')
        print('|'' '' ''/|\\')
        print('|'' '' '' ''/\\')
        print('|')
        print(escondida)
        quantidade = 6
    elif tentativa not in palavra and quantidade == 6:
        print('Você perdeu!!')
        print('|''-''-''-''-')
        print('|'' '' '' ''O')
        print('|   ---')
        print('|'' '' ''/|\\')
        print('|'' '' '' ''/\\')
        print('|')
        quantidade = 7