"""
Lissandra possui 2 avaliações no semestre: a P1 e a P2, e precisa saber se está ou não aprovada depois de realizar as suas provas.
Lissandra precisa ter média igual ou maior do que 5 para ser considerada aprovada.

Faça um programa em Python que leia as notas P1 e P2 de Lissandra e calcule a sua média utilizando a fórmula (P1 * 40% + P2 * 60%), e que atenda aos seguintes critérios:

-Caso a média obtida seja suficiente para a aprovação, informe na tela que Lissandra está aprovada.
-Caso contrário, informe que a média de Lissandra não foi suficiente e peça para ela informar a nota da prova de recuperação P3.
-Após ler a nota de recuperação da avaliação P3, substitua por uma das notas anteriores (P1 ou P2), de modo que Lissandra obtenha a maior nota no final.
-Se mesmo assim Lissandra não obtiver média suficiente, informe na tela que Lissandra está reprovada.

"""

#input do usuário
P1 = float(input("Insira sua nota P1: "))
P2 = float(input("Agora insira sua nota P2: "))

nome = input("\nQual o seu nome? ")

#cálculo MF
mediaFinal = P1 * 0.4 + P2 * 0.6

#cálculo P3
def calcP3():
    optP3 = input(f'{nome}, infelizmente uma média de {mediaFinal} te deixará de recuperação.\nDeseja fazer a P3? (s/n)')

    if optP3 == 's':
        calcP3.notaP3 = float(input('Insira sua nota de P3: '))
    elif optP3 == 'n':
        print('Ok! Boa sorte no próximo semestre!')
        return 0
    else:
        print('\nResponda com "s" para sim, e "n" para não.')
        Reset()
    return
def Reset():
    calcP3()

#saída caso aprovado
if mediaFinal >= 5:
    print(f"\nParabéns, {nome}! Você passou com uma média final de: {round(mediaFinal, 2)}")

#mudança teste
else:
    calcP3()

    if calcP3.notaP3 > P1:
        P1 = calcP3.notaP3

    elif calcP3.notaP3 > P2:
        P2 = calcP3.notaP3

    mediaFinal = P1 * 0.4 + P2 * 0.6
    if mediaFinal >= 5:
        print(f"\nParabéns, {nome}! Você passou com uma média final de: {round(mediaFinal, 2)}")
    else:
        print(f'{nome}, infelizmente você foi reprovado. Boa sorte no próximo semestre!')

#Código por: Felipe Louzada Guedes Carneiro da Fontoura - Matrícula: 2112130011