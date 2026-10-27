obstacles = int(input("How many obstacles must I avoid? "))

count = 0

while count < obstacles:
    print("Avoiding...")
    count = count + 1
    print(f"...Done! {count} obstacles avoided!")

print("All obstacles have been avoided.")
