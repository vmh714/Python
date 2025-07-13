PRESENT_YEAR = 2025
#Input information
name = input("Enter full your name: ")
year_birth = int(input("Enter your year of birth: "))
gpa = float(input("Enter your GPA: "))

#Process
age = PRESENT_YEAR - year_birth
if gpa >= 8.5:
    grade = "Excelent"
elif gpa >= 6.5:
    grade = "Good"
elif gpa >= 5.0:
    grade = "Average"
else :
    grade = "Poor"
#OUTPUT

print(f"Hello {name}, your age is {age}. Your GPA is {gpa}, grade is {grade}.")

