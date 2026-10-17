print("What is your name?")
name = input()
print(f"Wypierdalaj, {name}!")


email = input("WHAT IS YOUR EMAIL?: ")
print(f"Thank you: {name}")

phone_number = int(input("WHAT IS YOUR PHONE NUMBER?: "))
print(f"Thank you: {name}")

Dob = input("WHAT IS YOUR DATE OF BIRTH?: ")
print(f"Thank you: {name}") 

# save the data to a file

with open("../week 1/data/user_data.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Email: {email}\n")
    file.write(f"Phone Number: {phone_number}\n")
    file.write(f"Date of Birth: {Dob}\n")
