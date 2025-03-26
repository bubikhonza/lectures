books = [
    {
        "name": "Pán prstenů: Společenstvo prstenu",
        "price": 500,
        "author": "J.R.R. Tolkien",
        "publication_year": 1954,
    }
]

# 1: Přidej do proměnné 'books' 2 libovolné knihy, údaje mohou být libovolné. Vypiš list.
books.append({
    "name": "Sapiens: A Brief History of Humankind",
    "price": 350,
    "author": "Yuval Noah Harari",
    "publication_year": 2011,
})

books.append({
    "name": "Atomic Habits",
    "price": 400,
    "author": "James Clear",
    "publication_year": 2018,
})
print(books)

# 2. Změň cenu jedné libovolné knihy. Vypiš list.
books[0]["price"] = 999
print(books)

# 3. Odstraň nějakou knihu. Vypiš list.
books.pop()
print(books)

# 4. Vypiš celkový počet knih v listu.
print(len(books))


# Bonusový úkol (dobrovolné): Přidej 1 knihu pomocí uživatelského vstupu (https://www.w3schools.com/python/ref_func_input.asp)
name = input("Enter name: ")
price = int(input("Enter price: "))
author = input("Enter author: ")
year = int(input("Enter year: "))
books.append({
    "name": name,
    "price": price,
    "author": author,
    "publication_year": year,
})
print(books)