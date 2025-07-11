import matplotlib.pyplot as plt
import seaborn as sns


students = ["Ayush","John","Meena"]
marks = [95,88,78]

plt.bar(students,marks,color="skyblue")
plt.title("Student Marks")
plt.ylabel("Marks")
plt.xlabel("Students")
plt.show()