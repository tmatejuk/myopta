for i in range(10):
    for j in range(10):
        print((i+1)*(j+1), " ",end="")
    print("")

for i in range(10):
    for j in range(10):
        value = (i+1)*(j+1)
        print('{:04d}'.format(value), " ",end="")
    print("") 

for i in range(10):
    for j in range(10):
        value = (i+1)*(j+1)
        print('{:4d}'.format(value), end="")
    print("") 


#formating : https://pyformat.info/