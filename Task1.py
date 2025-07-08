age = int(input("Enter your age: "))

if age < 13:
    print("You are a minor.")
elif age < 19 and age >= 13:
    print("You are an adult.")