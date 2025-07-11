import matplotlib.pyplot as plt
import seaborn as sns


students = ["Ayush","John","Meena"]
marks = [95,88,78]

plt.bar(students,marks,color="skyblue")
plt.title("Student Marks")
plt.ylabel("Marks")
plt.xlabel("Students")
plt.show()

labels = ["Python", "Java", "C++"]
sizes = [60, 25, 15]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Language Popularity")
plt.show()
