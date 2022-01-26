"""
1. Defina em Python um novo tipo denominado t_pessoa que contenha as seguintes características:
• nome: String (tamanho 100),
• idade: inteiro,
• salário: real, e
• status: inteiro (0 - indica inativo; e 1 - indica ativo)
"""
t_pessoa = { "nome": "", "idade": 0, "salario": 0.0, "status": 0 }
print(t_pessoa)

t_pessoa = ["Felipe", 18, 600.0, 1]
print(t_pessoa)

"""
2. Implemente a função ler_pessoa(t_pessoa *p), que permite ler todos os dados relativos a uma
determinada pessoa. Considere que toda nova pessoa é inicializada com status 1 - ativo.
"""
def ler_pessoa():

    return