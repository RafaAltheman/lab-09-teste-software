from carrinho import total_com_desconto


def test_total_positivo():
    assert total_com_desconto([10, 20, 30, 40, 50]) > 0