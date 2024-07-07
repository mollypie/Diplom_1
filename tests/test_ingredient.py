import pytest

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
        ingredient = Ingredient(ingredient_type, 'плазмилли', 50)
        assert ingredient.type == ingredient_type

    def test_name_of_ingredient_true(self):
        ingredient = Ingredient('начинка', 'плазмилли', 50)
        assert ingredient.name == 'плазмилли'

    def test_price_of_ingredient_true(self):
        ingredient = Ingredient('начинка', 'плазмилли', 50)
        assert ingredient.price == 50

    def test_get_price_return_ingredient_price(self):
        ingredient = Ingredient('начинка', 'плазмилли', 50)
        assert ingredient.get_price() == 50

    def test_get_name_return_ingredient_name(self):
        ingredient = Ingredient('начинка', 'плазмилли', 50)
        assert ingredient.get_name() == 'плазмилли'

    def test_get_type_return_ingredient_type(self):
        ingredient = Ingredient('начинка', 'плазмилли', 50)
        assert ingredient.get_type() == 'начинка'
