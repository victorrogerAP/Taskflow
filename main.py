from tarefas import (
    adicionar_tarefa,
    listar_tarefas,
    buscar_tarefa,
    editar_tarefa,
    excluir_tarefa,
    filtrar_status
)
from database import inicializar_banco


def exibir_menu():
    menu = print("=========================\n"\
        "\n         TASKFLOW       \n"\
        "\n=========================\n"\
        "1 - Listar tarefas\n"\
        "2 - Adicionar tarefa\n"\
        "3 - Editar tarefa\n"\
        "4 - Excluir tarefa\n"\
        "5 - buscar tarefa\n"\
        "6 - Sair \n"\
        "7 - Filtrar status\n"\
        "\n=========================\n")
    return menu
      
    
def obter_opcao():
    while True:
        try:
            opcao = int(input("Escolheu a opção: "))
            return opcao
        except ValueError:
            print("Digite apenas números!")
            continue
            

def executar_opcao(opcao):
    match opcao:
        case 1:
            listar_tarefas()
        case 2:
            adicionar_tarefa()
        case 3:
            editar_tarefa()
        case 4:
            excluir_tarefa()
        case 5:
            buscar_tarefa()
        case 6:
            print("\nEncerrando o TaskFlow...")
            return False
        case 7:
            filtrar_status()
        case _:
            print("Opção inválida!")
    return True

inicializar_banco()
executador = True
while executador:
    exibir_menu()
    opcao = obter_opcao()
    executador = executar_opcao(opcao)

