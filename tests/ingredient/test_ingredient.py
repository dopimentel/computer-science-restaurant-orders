from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("queijo mussarela")
    assert ingredient.name == "queijo mussarela"
    assert ingredient.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
    invalid_ingredient = Ingredient("tomate")
    invalid_ingredient2 = Ingredient("tomate")
    invalid_ingredient3 = Ingredient("farinha de tomate")
    assert ingredient != invalid_ingredient
    assert invalid_ingredient == invalid_ingredient2
    assert invalid_ingredient2 != invalid_ingredient3
    assert hash(invalid_ingredient) == hash(invalid_ingredient2)
    assert hash(invalid_ingredient) != hash(invalid_ingredient3)
    expected = "Ingredient('queijo mussarela')"
    assert repr(ingredient) == expected
