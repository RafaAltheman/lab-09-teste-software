from classificacao import classificar_aluno


def test_aluno_aprovado():
    assert classificar_aluno(8.0, 80) == "Aprovado"


def test_aluno_reprovado_por_nota():
    assert classificar_aluno(3.0, 90) == "Reprovado"