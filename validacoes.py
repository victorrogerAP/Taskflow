
def validar_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto == "":
            print("O campo não pode ficar vazio!")
            continue
        break
    return texto


def validar_prioridade():
    prioridade = ["baixa", "alta","média"]
    while True:
        busca_prioridade = input("Qual prioridade deseja: ").strip().lower()
        if busca_prioridade not in prioridade:
            print("Prioridade inválida!")
            continue
        return busca_prioridade

        
def validar_status():
    status = ["pendente","em andamento","concluída"]
    while True:
        buscar_status = input("Qual status deseja: ").strip().lower()
        if buscar_status not in status:
            print("Status inválido!")
            continue
        return buscar_status
