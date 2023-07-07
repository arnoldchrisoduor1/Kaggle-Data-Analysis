import pandas as pd

ingredients = pd.Series(["2 cups", "three", "spoons", "pinches"],
                        index = ["Water", "Eggs", "Sugar", "Salt"], name = "Dinner")

print(ingredients)