book_cover = input("Enter the book cover type (hard/soft): ")

if book_cover == "soft":
    bound = input("Is the book perfect bound? (yes/no): ")
    if bound == "yes":
        print("The book is a softcover with perfect binding.")
    else:
        print("The book is a softcover without perfect binding.")
else:
    print("The book is a hardcover.")