def pretty_print_unordered(to_print):
    for item in to_print:
        print("* " + str(item))

def pretty_print_ordered(to_print):
    i = 1
    for item in to_print:
        print(str(i) + ". " + str(item))
        i+=1

def pretty_print_ordered2(to_print):
    for i in range(len(to_print)):
        print(str(i+1) + ". " + str(to_print[i]))

def pretty_print_ordered3(to_print):
    for i, item in enumerate(to_print,1):
        print(str(i) + ". " + str(item))

favorites=[]

more_items=True
while more_items:
    user_input=input("what is your favorite food? ")
    if user_input == '':
        more_items = False
    else:
        favorites.append(user_input)


print("here are all things you like!")
pretty_print_unordered(favorites)
pretty_print_ordered(favorites)
pretty_print_ordered2(favorites)
pretty_print_ordered3(favorites)
