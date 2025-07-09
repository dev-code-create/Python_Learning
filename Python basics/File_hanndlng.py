with open("data.txt", "w") as file:
    file.write("Hello! This is my first file.")

#appending text to the file
with open("data.txt", "a") as file:
    file.write("\nAdding more text.")

#Reading the content of the file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

