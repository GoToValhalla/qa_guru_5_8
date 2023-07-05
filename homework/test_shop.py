import pytest


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(-1) is False
        assert product.check_quantity(0) is True
        assert product.check_quantity(1) is True
        assert product.check_quantity(999) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(1)
        assert product.quantity == 999
        product.buy(999)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    # проверки на метод add_product
    def test_add_product(self, product, second_product, cart):
        cart.add_product(product)
        assert cart.products[product] == 1
        cart.add_product(product, 999)
        assert cart.products[product] == 1000
        assert len(cart.products) == 1
        # добавить другой товар
        cart.add_product(second_product, 10)
        assert cart.products[second_product] == 10
        assert len(cart.products) == 2

    # проверка на метод remove_product
    def test_remove_product(self, product, second_product, cart):
        cart.add_product(product, 200)
        cart.add_product(second_product, 1)
        cart.remove_product(product, 1)
        assert cart.products[product] == 199
        assert len(cart.products) == 2
        # remove_count больше, чем количество продуктов во второй позиции
        cart.remove_product(second_product, 2)
        assert len(cart.products) == 1
        # remove_count не передан
        cart.remove_product(product)
        assert len(cart.products) == 0
        # добавить проверку на удаление такого же количества товара, которое находиться в корзине
        cart.add_product(product, 300)
        cart.remove_product(product, 300)
        assert len(cart.products) == 0

    # проверка на метод clear
    def test_clear_cart(self, product, cart):
        cart.add_product(product, 100)
        cart.clear()
        assert len(cart.products) == 0

    # проверка на метод get_total_price
    def test_get_total_price(self, product, second_product, cart):
        cart.add_product(product, 100)
        cart.add_product(second_product, 10)
        assert (cart.get_total_price()) == 10150

    # проверка на метод buy
    def test_buy_products(self, product, second_product, cart):
        cart.add_product(product, 100)
        cart.add_product(second_product, 10)
        cart.buy()
        assert len(cart.products) == 0

    def test_buy_incorrect_quantity(self, product, cart):
        # купить больше, чем положили в корзину
        with pytest.raises(ValueError):
            cart.add_product(product, 1001)
            cart.buy()
