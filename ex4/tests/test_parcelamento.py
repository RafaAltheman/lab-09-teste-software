import pytest

from parcelamento import parcela


@pytest.mark.parametrize(
    ("valor", "n", "esperado"),
    [
        (100, 1, 100.00),
        (100, 2, 50.00),
        (100, 3, 33.33),
        (100, 4, 25.50),
        (100, 11, 10.55),
        (100, 12, 9.83),
        (100, 5, 20.80),
        (100, 6, 17.67),
        (100, 10, 11.40),
        (0, 4, 0.00),
        (1, 3, 0.33),
        (1, 12, 0.10),
        (25.50, 4, 6.50),
        (99.99, 4, 25.50),
    ],
)
def test_parcelas_validas(valor, n, esperado):
    assert parcela(valor, n) == esperado


@pytest.mark.parametrize("n", [-1, 0, 13, 14])
def test_parcelas_invalidas(n):
    with pytest.raises(ValueError, match=r"^parcelas invalidas$"):
        parcela(100, n)