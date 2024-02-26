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
                name = row["dish"]
                price = float(row["price"])
                ingredient = Ingredient(row["ingredient"])
                amount = int(row["recipe_amount"])

                dish = Dish(name, price)
                if dish not in self.dishes:
                    dish.add_ingredient_dependency(ingredient, amount)
                    self.dishes.add(dish)
                else:
                    for dish in self.dishes:
                        if dish.name == name:
                            dish.add_ingredient_dependency(ingredient, amount)


if __name__ == "__main__":
    menu = MenuData("data/menu_base_data.csv")
    for dish in menu.dishes:
        print(dish)
