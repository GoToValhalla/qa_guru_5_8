import pytest
from .models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def second_product():
    return Product("magazine", 15, "This is a magazine", 500)


@pytest.fixture
def cart():
    return Cart()