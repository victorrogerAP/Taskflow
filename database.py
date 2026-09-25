import sqlite3

def conectar_banco():
    conexao = sqlite3.connect("taskflow.db")
    return conexao


def inicializar_banco():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT NOT NULL,
            prioridade TEXT NOT NULL,
            status TEXT NOT NULL)
    """)
    conexao.commit()
    conexao.close()


def listar_tarefas_db():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT * FROM tarefas
    """)
    resultado = cursor.fetchall()
    conexao.close()
    return resultado


def adicionar_tarefa_db(titulo, descricao, prioridade, status):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO tarefas (titulo, descricao, prioridade, status)
        VALUES (?, ?, ?, ?)
    """, (titulo, descricao, prioridade, status))

    conexao.commit()
    conexao.close()


def atualizar_status_db(id_tarefa, status):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE tarefas
        SET status = ?
        WHERE id = ?
    """, (status, id_tarefa))
    conexao.commit()
    quantidade = cursor.rowcount
    conexao.close()
    return quantidade


def atualizar_titulo_db(id_tarefa, titulo):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(""" 
        UPDATE tarefas
        SET titulo = ?
        WHERE id = ?
    """,(titulo, id_tarefa))

    conexao.commit()
    quantidade = cursor.rowcount
    conexao.close()
    return quantidade

    
def atualizar_descricao_db(id_tarefa, descricao):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(""" 
        UPDATE tarefas
        SET descricao = ?
        WHERE id = ?
    """,(descricao, id_tarefa))

    conexao.commit()
    quantidade = cursor.rowcount
    conexao.close()
    return quantidade


def atualizar_prioridade_db(id_tarefa, prioridade):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(""" 
        UPDATE tarefas
        SET prioridade = ?
        WHERE id = ?
    """,(prioridade, id_tarefa))

    conexao.commit()
    quantidade = cursor.rowcount
    conexao.close()
    return quantidade


def excluir_tarefa_db(id_tarefa):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        DELETE FROM tarefas
        WHERE id = ?
    """,(id_tarefa,))
    conexao.commit()
    quantidade = cursor.rowcount
    conexao.close()
    return quantidade


def verificar_id_db(id_tarefa):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT id FROM tarefas WHERE id = ?
    """, (id_tarefa,))
    verifica_id = cursor.fetchone()
    conexao.close()
    return bool(verifica_id)
    
    
def busca_tarefa_db(titulo):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(""" 
    SELECT * FROM tarefas
    WHERE titulo LIKE ?
    """,(f"%{titulo}%",))

    resultado = cursor.fetchall()
    conexao.close()
    return resultado


def filtrar_status_db(status):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(""" 
    SELECT * FROM tarefas
    WHERE status = ?
    """,(status,))

    resultado = cursor.fetchall()
    conexao.close()
    return resultado