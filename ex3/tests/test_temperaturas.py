import pytest

from temperaturas import maior, dia_do_maior


@pytest.mark.parametrize(
    ("temps", "temp_max", "posicao"),
    [
        ([21, 25, 19, 30, 22], 30, 3),
        ([18], 18, 0),
        ([30, 21], 30, 0),
        ([30, 21, 30], 30, 0),
        ([18, 18], 18, 0),
        ([20, 25, 25, 10], 25, 1),
        ([1, 9, 2], 9, 1),
        ([-5, -10, -5], -5, 0),
        ([1, 2, 3, 4], 4, 3),
        ([7, 7, 7], 7, 0),
    ],
)
def test_maior_e_primeiro_dia(temps, temp_max, posicao):
    assert maior(temps) == temp_max
    assert dia_do_maior(temps) == posicao


@pytest.mark.parametrize("funcao", [maior, dia_do_maior])
def test_lista_vazia_com_mensagem(funcao):
    with pytest.raises(ValueError, match=r"^lista vazia$"):
        funcao([])