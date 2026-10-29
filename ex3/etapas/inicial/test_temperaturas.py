import pytest

from temperaturas import maior, dia_do_maior


@pytest.mark.parametrize(
    ("temps", "temp_max", "posicao"),
    [
        ([21, 25, 19, 30, 22], 30, 3),
        ([18], 18, 0),
        ([30, 21], 30, 0),
    ],
)
def test_funcoes_com_listas_iniciais(temps, temp_max, posicao):
    assert maior(temps) == temp_max
    assert dia_do_maior(temps) == posicao


@pytest.mark.parametrize("funcao", [maior, dia_do_maior])
def test_lista_vazia(funcao):
    with pytest.raises(ValueError):
        funcao([])