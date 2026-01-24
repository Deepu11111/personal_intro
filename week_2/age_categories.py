age = int(input("Enter your age : "))

if age < 13 :
    print("Category : Child")
elif 13 <= age <= 19:
    print("Category : TeenAger")
elif 20 <= age <= 64:
    print("Category : adult")
else:
    print("Category : Senior citizen")