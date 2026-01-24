def get_grade_info(marks):
    if marks >=90:
        return "A","Outstanding ! you are a great student"
    elif marks >=80:
        return "B", "Very Good! Keep it up"
    elif marks >=70:
        return "C","Good job ! need some more afforts"
    elif marks >=60:
        return "D","You just passed "
    else:
        return "E","Do not give up , you can do it !"
    
def main():
    print(" Student Grade Calculator")
    name = input("Enter Student name : ")

        #while loop for input validation (0-100)
    while True:
        try :
            marks = float(input("Enter marks (0-100): "))

            if 0 <= marks <= 100:
                break
            else:
                print("Invalid ! marks must be b/w 0 and 100.")
        except ValueError:
            print("Error ! please enter numbers only.")
    # here we are calling our function
    grade ,message = get_grade_info(marks)

    #final output
    print(f"\n Result for {name.upper()}:")
    print("-"*25)
    print(f"Marks : {marks}/100")
    print (f"Grade : {grade}")
    print(f"Message : {message}")
    print("-"*25)

#program start
if __name__ == "__main__":
  main() 

