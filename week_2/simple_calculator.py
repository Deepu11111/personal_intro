num_1 = float(input("Enter the first number : "))
oprtr = input("Enter the operator(+,-,*,/): ")
num_2 = float(input("Enter the Second number : "))

if oprtr == "+":
    print(f"Result:{num_1+num_2}")
elif oprtr == "-":
    print(f"Result :{num_1 - num_2}")
elif oprtr == "*":
    print(f"Result : {num_1 * num_2}")
elif oprtr == "/":
    if num_2 != 0:
        print(f"Result : {num_1 / num_2}")
    else:
        print("Error !!!, we can divide by zero..")
else:
    print("wrong operator...")