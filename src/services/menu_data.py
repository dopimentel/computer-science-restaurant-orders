# Req 3
import csv

from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.data = []
        self.dishes = set()
        with open(source_path, "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                dish_name = row["dish"]
                dish_price = float(row["price"])
                ingredient_name = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                dish = Dish(dish_name, dish_price)

                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, recipe_amount)

                if dish not in self.dishes:
                    self.dishes.add(dish)


if __name__ == "__main__":
    menu = MenuData("data/menu_base_data.csv")
    for dish in menu.dishes:
        print(repr(dish))
