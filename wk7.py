#Get student grade input 
grade = int(input("Enter the student's grade (0 -100): "))

#Check and print the grade
if grade >=80:
    print("Grade: A")
elif grade >=70:
    print("Grade: B")
elif grade >=60:
    print("Grade: C")
elif grade >=50:
    print("Grade: D")
else:
    print("Grade: F")
