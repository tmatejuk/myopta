def add(x,y):
    return (x+y)

while True:
    x = 0
    y = 0
    
    print("Which numbers do you want to add?")
    try:
        x = int(input("give first number : "))
    except:
        print("podanej wartosci nie mozna zamienic na liczbe")

    try:
        y = int(input("give first number : "))
    except:
        print("podanej wartosci nie mozna zamienic na liczbe")

    print("sum is : ", add(x,y))

