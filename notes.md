most of work was done with python version:
```
$ python --version
Python 3.10.12
```

## chapter 1
Setting Up Your Workspace :
(!) Don't skip this section! You need to make sure everything is set up properly
before you begin working on the code in this book. A lot of problems await
you if you have an improper configuration.

Python 3.5.1 +
python install and 

## chapter 2
Create your first module, navigate to your root directory and create an empty file called `game.py` .

## chapter 3
strings:
```
1 name = 'Phillip'
2 forecast = "It's going to rain!"
3 url = 'http://letstalkdata.com'
```

integers:
```
1 a = 3
2 b = 4
3 hypotenuse = 5
```

floating point:
```
1 a = 3.0
2 b = 4.0
3 hypotenuse = 5.0
```

do you understand:
```
n = 5
print(n)
print('n')
```

## chapter 4
```
print("Escape from Cave Terror!")
action_input = input('Action: ')
if action_input == 'n' or action_input == 'N':
   print("Go North!")
elif action_input == 's' or action_input == 'S':
   print("Go South!")
elif action_input == 'e' or action_input == 'E':
   print("Go East!")
elif action_input == 'w' or action_input == 'W':
   print("Go West!")
else:
   print("Invalid action!")
```

## chapter 5
functions

## chapter 6
lists
```
students = ['John', 'Jack', 'Ashton', 'Loretta']
list1 = ['Buffalo', 'Buffalo', 'Buffalo', 'Buffalo', 'Buffalo']
```

```
#add
>>> my_list = ['A','B','C']
>>> my_list.append('D')
```

```
#length
>>> my_list = ['A','B','C']
>>> len(my_list)
```

```
#index
>>> my_list = ['A', 'B', 'C', 'D']
>>> my_list[0]
```

```
#last
>>> my_list = ['A', 'B', 'C', 'D']
>>> last_position = len(my_list) - 1
>>> my_list[last_position]
D
```

```
#search
>>> 2 in [1, 2, 3]
True
>>> 5 in [1, 2, 3]
False
>>> 'A' in ['A', 'B', 'C']
True

>>> my_list = ['John', 'Jack', 'Ashton', 'Loretta']
>>> my_list.index('Ashton')
2

#first returned
>>> my_list = ['Buffalo', 'Buffalo', 'Buffalo']
>>> my_list.index('Buffalo')
0

#cannot be found
>>> my_list = ['John', 'Jack', 'Ashton', 'Loretta']
>>> my_list.index('Buffalo')
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
ValueError: 'Buffalo' is not in list
```

## chapter 07
loops

Python :
- a while loop 
- a for-each loop

>> As it turns out, the only loop you really need is a while loop.
>> However, many programming languages provide other looping
>> keywords to make writing loops easier.

using range:
```
1 def pretty_print_ordered(to_print):
2 for i in range(len(to_print)):
3 print(str(i + 1) + ". " + str(to_print[i]))
```

using enumarate
```
# tuple
1 first_name, last_name = ('Barack', 'Obama')
2 month, day, year = (10, 22, 2015)
3 dna_aminos = ('A','T','C','G')
```

```
1 def get_date():
2 return (10, 22, 2015)
3
4 date = get_date()
5 print(date)
```

```
def get_date():
2 return (10, 22, 2015)
3
4 month, day, year = get_date()
5 print(month)
```

If you pass a collection to the enumerate() function, you will get back a
special Python object that behaves like a list of tuples.
The object is called an iterator if you want to research more. The range() function also returns an iterator.


```
>>> letters = ['a', 'b', 'c']
>>> list(enumerate(letters))
[(0, 'a'), (1, 'b'), (2, 'c')]
>>> list(enumerate(letters, 1))
[(1, 'a'), (2, 'b'), (3, 'c')]
```

```
1 def pretty_print_ordered(to_print):
2     for i, value in enumerate(to_print, 1):
3         print(str(i) + ". " + str(value))
```

loop nesting:
```
for i in range(1,11):
    factors = []
        for j in range(1, i + 1):
            if i % j == 0:
                factors.append(j)
        print("The factors of " + str(i) + " are: " + str(factors))
```

Just like using i is a convention, j is a convention in a nested loop. If you really need them, k and l are next.

## chapter 8

objects

define a class, we use the class keyword followed by the name of the class,
which is TitleCased by convention

a special function that can be added to any Python object, called __init__()

a __str__() function that Python looks for when printing objects or when converting an object into a string using the str() function.

```
#format usage
def __str__(self):
    return "Name: " + self.name \
            + " Age: " + str(self.age) \
            + " Favorite food: " + str(self.favorite_foods[0])
            
    return "Name: {} Age: {} Favorite food: {}".format(self.name, self.age, self.favorite_foods[0])
```

In computer programming, a principle that we should strive to follow is “Don’t repeat yourself!” or “DRY”.

Two important concepts in OOP are composition and inheritance. 

Composition is when an object contains another object.

Inheritance is when a class inherits behavior from another class.

## chapter 9
exceptions

```
def most_powerful_weapon(inventory):
    max_damage = 0
    best_weapon = None
    for item in inventory:
        try:
            if item.damage > max_damage:
                best_weapon = item
                max_damage = item.damage
        except AttributeError:
            pass
    return best_weapon

play()
```

Raising Exceptions Intentionally

It may seem counter-intuitive at first, but there are some scenarios where we actually want to cause an exception to be raised.

We usually do this when we want to yell at ourselves for doing something wrong! Putting in checks for bad code will help us catch errors during testing.

To prevent ourselves from accidentally creating Weapon objects, we can
raise an exception in the initializer.
```
class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")
    def __str__(self):
        return self.name
```

## chapter 10

