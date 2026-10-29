from carrinho import total_com_desconto


def test_total_exato_sem_trocar_a_entrada():
    assert total_com_desconto([10, 20, 30, 40, 50]) == 141.00