# about creating a dictionary about students and their grades
# students names = Yash, Sandeep, Alice, Bob

dictionary = {"Yash": 100, "Sandeep": 90, "Alice": 85, "Bob": 88}
name = input("Enter the student's name: ")
if name in dictionary:
    print(f"{name}'s marks: {dictionary[name]}")
else:
    print("Student not found")