import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 2
def test_dish():
    dish = Dish("pizza", 50.0)
    assert dish.name == "pizza"
    assert dish.price == 50.0
    assert dish.recipe == {}
    assert dish.get_restrictions() == set()
    assert dish.get_ingredients() == set()

    with pytest.raises(TypeError):
        Dish("pizza", "50.0")
    with pytest.raises(ValueError):
        Dish("pizza", -1)

    dish.add_ingredient_dependency(Ingredient("queijo mussarela"), 1)
    assert dish.recipe == {Ingredient("queijo mussarela"): 1}

    dish2 = Dish("pizza", 50.0)
    assert dish == dish2
    assert hash(dish) == hash(dish2)
    dish3 = Dish("pizza", 50.1)
    assert dish != dish3
    assert hash(dish) != hash(dish3)

    expected = "Dish('pizza', R$50.00)"
    assert repr(dish) == expected
