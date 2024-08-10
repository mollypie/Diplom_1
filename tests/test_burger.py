from unittest.mock import Mock

import pytest

from bun import Bun
from burger import Burger
from ingredient import Ingredient
from ingredient_types import *


class TestBurger:
    def test_set_buns_true(self):
        bun = Bun('Космическая', 400)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun.name == bun.name and burger.bun.price == bun.price

    def test_add_ingredient_true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'плазмилли', 50)
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) > 0

    def test_remove_ingredient_index_empty_list(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'плазмилли', 50)
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_index_changed(self):
        ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, 'плазмилли', 50)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, 'плазфффффмилли', 150)
        burger = Burger()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients.index(ingredient2) == 0

    @pytest.mark.parametrize(
        'bun_price, ingredient_price, total_price',
        [
            [500, 200, 1200],
            [150, 350, 650]
        ]
    )
    def test_get_price_return_price(self, bun_price, ingredient_price, total_price):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = ingredient_price

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients.append(mock_ingredient)

        assert burger.get_price() == total_price

    @pytest.mark.parametrize(
        'bun_name, bun_price, ingredient_type, ingredient_name, ingredient_price, burger_price',
        [
            ['sfs', 500, INGREDIENT_TYPE_SAUCE, 'hk', 200, 1200],
            ['sedfas', 100, INGREDIENT_TYPE_FILLING, 'ftfhf', 300, 500]
        ]
    )
    def test_get_receipt_return_receipt(self, bun_name, bun_price, ingredient_type, ingredient_name, ingredient_price, burger_price):
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_name.return_value = ingredient_name
        mock_ingredient.get_price.return_value = ingredient_price

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients.append(mock_ingredient)

        assert burger.get_receipt() == (f'(==== {bun_name} ====)'
                                        f'\n= {ingredient_type.lower()} {ingredient_name} ='
                                        f'\n(==== {bun_name} ====)\n'
                                        f'\nPrice: {burger_price}')
