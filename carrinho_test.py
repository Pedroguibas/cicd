from carrinho import calculate_total, apply_discount

def test_calculate_total():
    result = calculate_total(10, 3)
    assert result == 30

def test_apply_discount():
    result = apply_discount(100, 0.1)
    assert result == 90