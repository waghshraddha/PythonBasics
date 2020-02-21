#this program finds the greatest among three number

a = int(input("Enter no 1: "))
b = int(input("Enter no 2: "))
c = int(input("Enter no 3: "))

if a > b:
    if a > c:
        print("{} is Greater ".format(a))
    else:
            print("{} is Greater ".format(c))
else:
    if b > c:
        print("{} is Greater".format(b))
    else:
        print("{} is Greater".format(c))
