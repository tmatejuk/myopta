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
        for i in range(len(self.ingredients)):
            sum = sum + self.ingredients[i].calories()
        return sum

woda = Food("woda", 0, 0, 0)
owoce = Food("jablko",20,1,0)
owies = Food("platki owsiane",20,1,1)
mleko = Food("mleko 3.2",10,2,3)

owsianka = Recipe("owsianka",[woda,owoce,owies,mleko])
sok = Recipe("sok jablkowy",[woda,owoce])
mleko = Recipe("mleko", [mleko])

print("receptura : " + str(owsianka))
print("calorycznosc : ", owsianka.calories())

print("receptura : " + str(sok))
print("calorycznosc : ", sok.calories())

print("receptura : " + str(mleko))
print("calorycznosc : ", mleko.calories())

