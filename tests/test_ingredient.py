import pytest

from helpers import Helpers
from ingredient import Ingredient
from ingredient_types import *


class TestIngredient:
    @pytest.mark.parametrize(
        'ingredient_type',
        [
            [INGREDIENT_TYPE_FILLING],
            [INGREDIENT_TYPE_SAUCE]
        ]
    )
    def test_ingredient_type_true(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, Helpers.create_name(), Helpers.create_price())
        assert ingredient.type == ingredient_type

    def test_name_of_ingredient_true(self):
        ingredient_name = Helpers.create_name()
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, ingredient_name, Helpers.create_price())
        assert ingredient.name == ingredient_name

    def test_price_of_ingredient_true(self):
        ingredient_price = Helpers.create_price()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Helpers.create_name(), ingredient_price)
        assert ingredient.price == ingredient_price

    def test_get_price_return_ingredient_price(self):
        ingredient_price = Helpers.create_price()
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'плазмилли', ingredient_price)
        assert ingredient.get_price() == ingredient_price

    def test_get_name_return_ingredient_name(self):
        ingredient_name = Helpers.create_name()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, ingredient_name, Helpers.create_price())
        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize(
        'ingredient_type',
        [
            [INGREDIENT_TYPE_FILLING],
            [INGREDIENT_TYPE_SAUCE]
        ]
    )
    def test_get_type_return_ingredient_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, Helpers.create_name(), Helpers.create_price())
        assert ingredient.get_type() == ingredient_type
