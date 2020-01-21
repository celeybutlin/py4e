#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
sg= input("Enter Grade: ")
fg = float(sg)
if fg >= 1.0 or fg < 0:
    print("Please enter valid grade between 0 and 1.0")
    exit()
elif fg >= 0.9:
    print("A")
    exit()
elif fg >= 0.8:
    print("B")
    exit()
elif fg >= 0.7:
    print("C")
    exit()
elif fg >= 0.6:
    print("D")
    exit()
elif fg <= 0.5:
    print("F")
    exit()
