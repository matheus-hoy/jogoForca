print('Bem Vindo ao JOGO DA FORCA XD')
print('Você tem 6 chances')
print()
palavra_secreta = 'perfume'
digitado = []
chances = 6
while True:
    if chances <= 0:
        print('YOU LOSE')
        break

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
       print('Digite apenas uma letra Malandro')
       continue

    digitado.append(letra)

    if letra in palavra_secreta:
       print(f'Boa, a letra "{letra}" faz parte da Palavra secreta.')
    else:
         print(f'Putz, a letra "{letra}" não faz parte da Palavra secreta.')
         digitado.pop()


    secreto_temporario = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in digitado:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario+= '*'

    if secreto_temporario == palavra_secreta:
        print('PARABÉNS, VOCÊ CONSEGUIU... IHAAAAA')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in palavra_secreta:
        chances -= 1

    print(f' Voce ainda pode tentar: {chances}x')
    print()




