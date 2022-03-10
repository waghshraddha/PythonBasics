def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("Select:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    Choice=input("Enter the choice 1 / 2 / 3/ 4:")

    if Choice in('1','2','3','4'):
        a=float(input("Enter first digit:"))
        b=float(input("Enter second digit:"))

        if Choice == '1':
            print(a,"+",b,"=", add(a,b))

        elif Choice == '2':
            print(a,"-",b,"=", subtract(a,b))

        elif Choice == '3':
            print(a,"*",b,"=", multiply(a,b))

        elif Choice == '4':
            print(a,"/",b,"=", divide(a,b))

        new_cal=input("Want a new calculation?(Yes/No):")
        if new_cal == "No":
            break
        else:
            print("Invalid Input")
