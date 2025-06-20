a=int(input("Enter a subject-1: "))
b=int(input("Enter a subject-2: "))
c=int(input("Enter a subject-3: "))
d=int(input("Enter a subject-4: "))

print("subject-1 marks:",a)
print("\nsubject-2 marks:",b)
print("\nsubject-3 marks:",c)
print("\nsubject-4 marks:",d)
total = a + b + c + d
print("Total marks:", total)
percentage = (total / 400) * 100
print("Percentage:", percentage)
if percentage >= 70:
    print("Grade: distinction")
elif percentage >= 60:
    print("Grade: first class")       
elif percentage >= 50:
    print("Grade: second class")   
elif percentage >= 40:
    print("Grade: pass class")
else:
    print("Grade: fail, better luck next time")