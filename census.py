class Person:
    def __init__(self, name, age, favorite_foods):
        self.name = name
        self.age = age
        self.favorite_foods = favorite_foods

    def __str__(self):
        #return "Name: " + self.name \
        #    + " Age: " + str(self.age) \
        #    + " Favorite food: " + str(self.favorite_foods[0])
        return "Name: {} Age: {} Favorite food: {}".format(self.name, self.age, self.favorite_foods[0])
    
    def birth_year(self):
        return 2015 - self.age

people = [Person("Ed",11,['hotdogs','jawbreakers']),
          Person("Eddy",19,['broccoli']),
          Person("Edward",29,['apple','chunky puffs'])]

age_sum = 0
year_sum = 0
for person in people:
    age_sum = age_sum + person.age
    year_sum = year_sum + person.birth_year()

print("The people polled in this census were:")
for person in people:
    print(person)

print("The average age is: " + str(age_sum/len(people)))
print("The average birth year is: " + str(int(year_sum / len(people))))
