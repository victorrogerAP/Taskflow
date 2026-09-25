from database import (adicionar_tarefa_db, 
                      listar_tarefas_db, 
                      busca_tarefa_db, 
                      atualizar_titulo_db,
                      atualizar_descricao_db,
                      atualizar_prioridade_db,
                      atualizar_status_db,
                      verificar_id_db,
                      excluir_tarefa_db,
                      filtrar_status_db)
from validacoes import validar_texto, validar_prioridade, validar_status

def adicionar_tarefa():
    print("\n===== ADICIONAR TAREFA =====")
    titulo = validar_texto("Digite o título: ")
    descricao = validar_texto("Digite a descrição: ")
    prioridade = validar_prioridade()
    status = validar_status()
    adicionar_tarefa_db(
            titulo,
            descricao,
            prioridade,
            status
        )
    print("\nTarefa adicionada com sucesso!")


def listar_tarefas():
    resultado = listar_tarefas_db()
    if not resultado:
       print("Nenhuma tarefa cadastrada")
       return
    exibir_tarefa(resultado)


def buscar_tarefa():
    print("\n===== BUSCAR TAREFA =====") 
    titulo = validar_texto("Qual tarefa procurar: ")
    resultado = busca_tarefa_db(titulo)
    if not resultado:
            print("Nenhuma tarefa cadastrada")
            return
    exibir_tarefa(resultado)


def editar_titulo(id_tarefa):
    novo_titulo = validar_texto("Digite o novo título: ")
    quantidade = atualizar_titulo_db(id_tarefa, novo_titulo)
    if quantidade == 1:
        print("Título atualizado com sucesso!")
    else:
        print("Nenhuma tarefa foi atualizada!")


def editar_descricao(id_tarefa):
    nova_descricao = validar_texto("Digite a nova descrição: ")
    quantidade = atualizar_descricao_db(id_tarefa, nova_descricao)
    if quantidade == 1:
        print("Descrição atualizada com sucesso!")
    else:
        print("Nenhuma tarefa foi atualizada!")


def editar_prioridade(id_tarefa):
    nova_prioridade = validar_prioridade()
    quantidade = atualizar_prioridade_db(id_tarefa, nova_prioridade)
    if quantidade == 1:
        print("Prioridade atualizada com sucesso!")
    else:
        print("Nenhuma tarefa foi atualizada!")


def editar_status(id_tarefa):
    novo_status = validar_status()
    quantidade = atualizar_status_db(id_tarefa, novo_status)
    if quantidade == 1:
        print("Status atualizado com sucesso!")
    else:
        print("Nenhuma tarefa foi atualizada!")


def exibir_tarefa(resultado):
    for tarefa in resultado:
        print("\n===== TAREFA ENCONTRADA =====") 
        print("ID:",tarefa[0])
        print("Título:",tarefa[1])
        print("Descrição:",tarefa[2])
        print("Prioridade:",tarefa[3])
        print("Status:",tarefa[4])


def editar_tarefa():
    print("\n===== EDITAR TAREFA =====") 
    while True:
        try:
            id_tarefa = int(input("Qual ID da tarefa?"))
            if verificar_id_db(id_tarefa):
                print("ID encontrado!")
                opcao_alteracao = int(input( "\nO que deseja alterar?\n" "1 - Título\n" "2 - Descrição\n" "3 - Prioridade\n" "4 - Status\n" "Escolha: " ))
                if opcao_alteracao <1 or opcao_alteracao > 4:
                    print("Opção inválida!")
                    continue
                if opcao_alteracao == 1:
                    editar_titulo(id_tarefa)
                elif opcao_alteracao == 2:
                    editar_descricao(id_tarefa)
                elif opcao_alteracao == 3:
                    editar_prioridade(id_tarefa)
                elif opcao_alteracao == 4:
                   editar_status(id_tarefa)
                break
            else:
                print("ID não encontrado!")
                continue
        except ValueError:
            print("Digite apenas números")


def excluir_tarefa():
    print("\n===== EXCLUIR TAREFA =====")
    while True:
        try:
            id_tarefa = int(input("Qual ID deseja excluir: "))
            quantidade = excluir_tarefa_db(id_tarefa)
            if quantidade == 1:
                print("Tarefa excluída com sucesso!")
                break
            else:
                print("ID não encontrado!")
                continue
        except ValueError:
            print("Digite apenas números!")


def filtrar_status():
    print("======== FILTRAR POR STATUS ========")
    status = validar_status()
    resultado = filtrar_status_db(status)
    if resultado:
        exibir_tarefa(resultado)
    else:
        print("Nenhuma tarefa encontrada com esse status!")