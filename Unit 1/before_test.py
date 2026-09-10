print("Welcome in your store")
total_price=0
number_books=0
books=[]
book_choice=input("Which book would u like to buy?: ").lower()
while book_choice!= "done":
    price_book=int(input("What is the price of this book in dollars?: "))
    total_price+=price_book
    number_books+=1
    books.append(book_choice)
    print(f"the {book_choice} book was added for {price_book} dollars")
    print(f"your total so far {total_price}")
    book_choice=input("Which book would u like to buy?: ").lower()

for book_choice in books:
    print(f"You have book: {book_choice}")

print(f"your final bill is {total_price}")
print(f"your number of books is {number_books}")
