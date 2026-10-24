first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

# count up the numbers ok even or odd
even_count = 0
odd_count = 0


if first_number % 2 == 0:
    even_count = even_count + 1
else: odd_count += 1

if second_number % 2 == 0:
    even_count += 1
else:odd_count += 1

if third_number % 2 == 0:
    even_count += 1
else:odd_count += 1

print(f"Even numbers count: {even_count}")
print(f"Odd numbers count: {odd_count}")
