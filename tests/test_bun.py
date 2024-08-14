from bun import Bun
from helpers import Helpers


class TestBun:
    def test_name_of_bun_true(self):
        bun_name = Helpers.create_name()
        bun = Bun(bun_name, Helpers.create_price())
        assert bun.name == bun_name

    def test_price_of_bun_true(self):
        bun_price = Helpers.create_price()
        bun = Bun(Helpers.create_name(), bun_price)
        assert bun.price == bun_price

    def test_get_name_return_bun_name(self):
        bun_name = Helpers.create_name()
        bun = Bun(bun_name, Helpers.create_price())
        assert bun.get_name() == bun_name

    def test_get_price_return_bun_price(self):
        bun_price = Helpers.create_price()
        bun = Bun(Helpers.create_name(), bun_price)
        assert bun.get_price() == bun_price
        