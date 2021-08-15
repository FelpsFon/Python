"""
Implemente um programa em Python3 que faça o seguinte:
- Solicite 3 número para o usuário e armazene em 3 variáveis diferentes.
- Some os 3 número e guarde o resultado em uma outra variável.
- Divida o resultado da soma anterior por 3 e guarde em uma nova variável.
- Solicite ao usuário o seu nome e salve em uma variável.
- Mostre o nome do usuário na tela assim como o resultado da operação, utilizando a seguinte mensagem: "<usuário>, a média entre os número é de <resultado_final>"
(subistitua <usuário> e <resultado_final> pelo nome do usuário e pelo resultado final da operação, respectivamente).
"""

#input do usuário
n1 = float(input("Insira o primeiro número: "))
n2 = float(input("\nAgora insira o segundo número: "))
n3 = float(input("\nE agora insira o terceiro número: "))

nome = input("\nQual o seu nome? ")

#cálculo
soma = n1 + n2 + n3
divisao = soma / 3

#saída
print(f"\n{nome}, a média dos números {n1}, {n2} e {n3} é de: {divisao}")
input('Aperte qualquer tecla para fechar...')

#Código por: Felipe Louzada Guedes Carneiro da Fontoura - Matrícula: 2112130011