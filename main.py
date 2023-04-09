from ops import *

N = 5
# declarando uma lista
lista = []

option = 2

while option >= 2 and option <= 4:
    print("""
    Menus das opções
    1 - Sair;
    2 - Inserir um elemento na linha; 
    3 - Remover um elemento da linha;
    4 - Consultar um elemento específico da linha;
    5 - Mostrar linha;
    """)
    #entrada de opcoes
    option = int(input("Digite a sua opção do menu: "))

    if option == 1:
        print("Saída realizada com sucesso")
        break

    elif option < 2 or option > 4:
        print("Comando Inválido, digite um número válido: ")
        
    match option:
        case 2: 
            x = str(input("Digite um valor a ser inserido a fila: "))
            stackup(x)
        case 3:
            unstack()
            print(line)
        case 4:
            c = (int(input("Valor a ser consultado: ")))
            consult(c)
        case 5:
            print(line)

    option = 2