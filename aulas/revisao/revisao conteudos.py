# from -> módulo ou biblioteca
# import -> classes, métodos e afins...
from abc import ABC, abstractmethod

# Criando qualquer classe, ela herda da classe object
class MinhaClasse(object): # class cria uma classe
    def __init__(self, idade, cpf): # def define uma função
        # variável -> atributo
        # podemos ter atributos públicos, privados __ e protegidos _
        # atributo público
        self.idade = idade # definindo atributo da classe MinhaClasse
        # atibuto privado
        self.__cpf = cpf
        pass # pass faz com que essa linha seja descartada na execução

    # getter e setter
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    # metodo define um bloco de código
    def funcao(self): # função -> método
        # print("Minha função está sendo executada")
        while True:
            # print("Iniciando loop infinito...")
            while True:
                def outraFuncao():
                    #outro bloco de código
                    pass
                # print("Iniciando outro while...")
                return 10
#objeto = MinhaClasse() # criando instãncia da classe MinhaClasse

#----------------------------------------------------------------
# Estruturas de Dados, imutabilidade, itegração

tupla = (10, 20, True) # imutável
lista = ["livro", 10, True]

produtos = [
    "Telefone",
    "Notebook",
    "Televisão",
    "Notebook",
    "Caixa de som",
    "Televisão"
]

# enumerate separa indices e valores
# for indice, valor in enumerate(produtos, start=1):
#     print(f'Indice {indice} | Valor {valor}')

# set retira valores repetidos
produtos_unicos = set(produtos)
# print(produtos)
# print(produtos_unicos)

dicionario_clientes = {
    "nome": "João",
    "email": "joao@gmail.com"
}

# get busca um valor e retorna None se não encontrar
telefone = dicionario_clientes.get("telefone", "Não tem telefone")
#print(f"Funcionario {dicionario_clientes.get("nome")}, numero: {telefone}")

# -------------------------------------------------------------------------
# Tratameto de exeções personalizadas
class IdadeInvalidaError(Exception):
    """
        Um erro customizado para ser lançado no meu
        tratamento de exceção.
    """
    pass

class Aluno:
    def __init__(self, nome, turma, idade):
        self.nome = nome
        self.turma = turma
        self.idade = idade

# class Main:
#     try:
#         aluno1 = Aluno("João", "Python", -22)
#         if aluno1.idade < 0:
#             aluno1.idade = 0
#             raise IdadeInvalidaError("Idade é menor do que 0.\nIDADE INVÁLIDA.")
#     except Exception as erro:
#         print(erro)

# -----------------------------------------------------
def calculo_imposto(valor, imposto):
    print("iniciando função...")
    valor_final = ((valor * imposto) / 100) + valor
    return valor_final
    print("Encerrando função...")

valor_imposto =  calculo_imposto(100, 15)

print(valor_imposto)

cliente = {
    "nome": "João",
    "telefone_1": "6199296-8787",
}
print(cliente['telefone_2'])











