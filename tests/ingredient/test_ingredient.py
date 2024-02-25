import pytest
from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


@pytest.fixture
def sample_ingredients():
    return [
        Ingredient("queijo mussarela"),
        Ingredient("farinha"),
        Ingredient("bacon"),
        Ingredient("manteiga"),
        Ingredient("caldo de carne"),
        # Ingredient("camarão"),
        # Ingredient("carne"),
        # Ingredient("creme de leite"),
        # Ingredient("frango"),
        # Ingredient("ovo"),
        # Ingredient("queijo gorgonzola"),
        # Ingredient("salmão"),
        # Ingredient("presunto"),
        # Ingredient("queijo parmesão"),
        # Ingredient("queijo provolone"),
        # Ingredient("massa de lasanha"),
        # Ingredient("massa de ravioli"),
    ]


# Req 1
def test_ingredient(sample_ingredients):
    for ingredient in sample_ingredients:
        assert isinstance(ingredient, Ingredient)
        assert repr(ingredient) == f"Ingredient('{ingredient.name}')"
        assert ingredient.name in [
            "queijo mussarela",
            "farinha",
            "bacon",
            "manteiga",
            "caldo de carne",
            # "camarão",
            # "carne",
            # "creme de leite",
            # "frango",
            # "ovo",
            # "queijo gorgonzola",
            # "salmão",
            # "presunto",
            # "queijo parmesão",
            # "queijo provolone",
            # "massa de lasanha",
            # "massa de ravioli",
        ]
        assert ingredient.restrictions in [
            {"LACTOSE", "ANIMAL_DERIVED"},
            {"GLUTEN"},
            {"ANIMAL_MEAT", "ANIMAL_DERIVED"},
            {"LACTOSE", "ANIMAL_DERIVED"},
            {"ANIMAL_DERIVED"},
            # {"ANIMAL_MEAT", "SEAFOOD", "ANIMAL_DERIVED"},
            # {"ANIMAL_MEAT", "ANIMAL_DERIVED"},
            # {"LACTOSE", "ANIMAL_DERIVED"},
            # {"ANIMAL_MEAT", "ANIMAL_DERIVED"},
            # {"ANIMAL_DERIVED"},
            # {"LACTOSE", "ANIMAL_DERIVED"},
            # {"ANIMAL_MEAT", "SEAFOOD", "ANIMAL_DERIVED"},
            # {"ANIMAL_MEAT", "ANIMAL_DERIVED"},
            # {"LACTOSE", "ANIMAL_DERIVED"},
            # {"LACTOSE", "ANIMAL_DERIVED"},
            # {"LACTOSE", "GLUTEN"},
            # {"LACTOSE", "GLUTEN"},
        ]
        for ingredient2 in sample_ingredients:
            if ingredient.name == ingredient2.name:
                assert ingredient == ingredient2
            else:
                assert ingredient != ingredient2
