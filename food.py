class Food:
    def __init__(self, name, carbs, protein, fat):
        self.name = name
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
    def __str__(self):
        return self.name
    def calories(self):
        return 4 * self.carbs + 4 * self.protein + 9 * self.fat

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
    def __str__(self):
        return self.name
    def calories(self):
        sum = 0
        for ingredient in self.ingredients:
            sum = sum + ingredient.calories()
        return sum

woda = Food(name="woda", carbs=0, protein=0, fat=0)
owoce = Food("jablko",20,1,0)
owies = Food("platki owsiane",20,1,1)
mleko = Food("mleko 3.2",10,2,3)

owsianka = Recipe("owsianka",[woda,owoce,owies,mleko])
sok = Recipe("sok jablkowy",[woda,owoce])
napoj_mleko = Recipe("mleko", [mleko])

recipes = [owsianka, sok, napoj_mleko]
for recipe in recipes:
    print("receptura : " + str(recipe))
    print("calorycznosc : ", recipe.calories())

