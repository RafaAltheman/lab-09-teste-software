import pytest

from carrinho import total_com_desconto


@pytest.mark.parametrize(
    ("precos", "esperado"),
    [
        ([10, 20, 30, 40, 50], 141.00),
        ([], 0.00),
        ([100], 100.00),
        ([10, 20, 30], 60.00),
        ([10, 20, 30, 40], 96.00),
        ([0, 0, 0, 0.03], 0.03),
        ([1.11, 2.22, 3.33, 4.44], 10.66),
        ([10, 20, 30, 0], 60.00),
        ([10, 20, 30, 0, 10], 69.00),
        ([0.10, 0.20, 0.30, 0.01], 0.61),
    ],
)
def test_total_com_desconto(precos, esperado):
    assert total_com_desconto(precos) == esperado