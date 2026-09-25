from validacoes import validar_prioridade, validar_texto


def test_validar_prioridade(monkeypatch):
    entradas = ["urgente", "alta"]
    monkeypatch.setattr("builtins.input", lambda _: entradas.pop(0))

    resultado = validar_prioridade()

    assert resultado == "alta"


def test_validar_texto(monkeypatch):
    entradas = ["", "Python"]
    monkeypatch.setattr("builtins.input", lambda _: entradas.pop(0))

    resultado = validar_texto()

    assert resultado == "Python"