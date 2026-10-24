first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
# program to decide which number is greater
if first_number > second_number:
    print(first_number, "is greater than", second_number)
elif first_number < second_number:
    print(first_number, "is less than", second_number)
else:
    print(first_number, "is equal to", second_number)  