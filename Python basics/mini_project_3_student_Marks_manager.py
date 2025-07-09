def add_student():
  name = input("Enter student name:")
  marks = input("Enter student marks:")

  with open("students.txt","a") as file:
   file.write(f"{name},{marks}\n")
   print("Student record added")

def view_students():
  print("\nStudents Records:")
  with open("students.txt","r") as  file:
    for line in file:
      name,marks = line.strip().split(",")
      print(f"Name: {name}, Marks: {marks}")

while True:
  print("\n1. Add Student")
  print("2. Show All Students")
  print("3. Exit")
  choice = input("Enter your choice (1-3): ")

  if choice == "1":
    add_student()
  elif choice == "2":
    view_students()
  elif choice == "3":
    print("Exiting the program.")
    break
  else:
    print("Invalid choice. Please try again.")
     