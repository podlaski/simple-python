try:
    a = 10
    b = int(input('Number: '))
    print(a/b)

except ZeroDivisionError:
    print("Error, please try again. You can't divide by zero.")
