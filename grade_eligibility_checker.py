# Get user input
student_name=input("Enter student name: ")
gpa=float(input("enter GPA (0.0-4.0): "))
credits=float(input("Enter tota credit hours: "))

# Dean's list requirements
required_GPA=3.5
required_credits=12

 # Check eligibility
eligible= (gpa >= required_GPA) and (credits >= required_credits)

# Display student information
print(f"\nStudent Name: {student_name}")
print(f"GPA: {gpa}")
print(f"Total Credit Hours: {credits}")
print(f"Dean's List Eligibility: {eligible}")

# Credits needed
if credits < required_credits:
    print(f"More credits needed: {required_credits-credits}")
else:
    print("Credit hour requirement met.")