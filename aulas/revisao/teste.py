class Pessoa(object):
    # Método construtor
    def __init__(self, nome): # parâmetro
        # atributo
        # privatos
        self.__nome = nome
        self.__senha = "1234"

    def mostrar_nome(self): # método público
        print(self.__nome)

pessoa1 = Pessoa("João de Menezes")
pessoa2 = Pessoa("Marcelo Oliveira")
pessoa1.mostrar_nome()
pessoa2.mostrar_nome()

print("tentando acessar atributo privado")
print(pessoa1._Pessoa__senha)