import pytest

from parcelamento import parcela


# Casos de valor-limite definidos antes das ferramentas.
@pytest.mark.parametrize(
    ("n", "esperado"),
    [
        (1, 100.00),
        (2, 50.00),
        (3, 33.33),
        (4, 25.50),
        (11, 10.55),
        (12, 9.83),
    ],
)
def test_limites_validos(n, esperado):
    assert parcela(100, n) == esperado


@pytest.mark.parametrize("n", [-1, 0, 13, 14])
def test_limites_invalidos(n):
    with pytest.raises(ValueError, match=r"^parcelas invalidas$"):
        parcela(100, n)