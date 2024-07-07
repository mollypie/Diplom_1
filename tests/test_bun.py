from bun import Bun


class TestBun:
    def test_name_of_bun_true(self):
        bun = Bun('Космическая', 400)
        assert bun.name == 'Космическая'

    def test_price_of_bun_true(self):
        bun = Bun('Космическая', 400)
        assert bun.price == 400

    def test_get_name_return_bun_name(self):
        bun = Bun('Космическая', 400)
        assert bun.get_name() == 'Космическая'

    def test_get_price_return_bun_price(self):
        bun = Bun('Космическая', 400)
        assert bun.get_price() == 400
        