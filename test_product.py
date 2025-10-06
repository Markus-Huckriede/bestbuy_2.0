import pytest
from products import Product

'''
create valid product
'''


def test_create_valid_product():
    p = Product("MacBook Air M2", price=1200.0, quantity=5)
    assert p.name == "MacBook Air M2"
    assert p.price == 1200.0
    assert p.quantity == 5
    assert p.is_active() is True


'''
empty name
'''


def test_product_invalid_name():
    with pytest.raises(ValueError):
        Product("", price=100, quantity=10)


'''
negative price
'''


def test_product_invalid_price():
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=10)


'''
negative quantity
'''


def test_product_invalid_quantity():
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=10, quantity=-10)


'''
makes product inactive when amount becomes zero
'''


def test_product_becomes_inactive():
    p = Product("Product", price=10, quantity=1)
    p.set_quantity(0)
    assert p.is_active() is False


'''
buying a product reduces amount in stock
'''


def test_buy_modifies_quantity():
    p = Product("Product", price=10, quantity=10)
    p.buy(5)
    assert p.quantity == 5


'''
buying a higher quantity than available in stock
'''


def test_buy_too_much():
    with pytest.raises(Exception):
        p = Product("Product", price=10, quantity=10)
        p.buy(12)
