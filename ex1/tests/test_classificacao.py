import pytest
from classificacao import classificar_aluno

@pytest.mark.parametrize(
    ("media", "presenca", "resultado"),
    [
        (8.0, 80, "Aprovado"),
        (3.0, 90, "Reprovado"),
        (7.0, 75, "Aprovado"),
        (10.0, 100, "Aprovado"),
        (6.99, 75, "Recuperacao"),
        (5.0, 75, "Recuperacao"),
        (4.99, 75, "Reprovado"),
        (0.0, 100, "Reprovado"),
        (9.0, 74.99, "Reprovado por falta"),
        (5.0, 0, "Reprovado por falta"),
        (8.0, 74, "Reprovado por falta"),
    ],
)
def test_classificacao_e_limites(media, presenca, resultado):
    assert classificar_aluno(media, presenca) == resultado


@pytest.mark.parametrize("media", [-0.01, 10.01, -1, 11])
def test_media_invalida(media):
    with pytest.raises(ValueError, match=r"^Media invalida$"):
        classificar_aluno(media, 80)


@pytest.mark.parametrize("presenca", [-0.01, 100.01, -1, 101])
def test_presenca_invalida(presenca):
    with pytest.raises(ValueError, match=r"^Presenca invalida$"):
        classificar_aluno(8.0, presenca)


def test_media_e_presenca_invalidas_prioriza_media():
    with pytest.raises(ValueError, match=r"^Media invalida$"):
        classificar_aluno(-1, -1)