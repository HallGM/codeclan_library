library = {
    "name": "CodeClan Library",
    "books": [
        {
            "author": "George RR Martin",
            "title": "A Song of Ice and Fire"
        },
        {
            "author": "J R. R. Tolkien",
            "title": "The Hobbit"
        },
        {
            "author": "Paul Barry",
            "title": "Head-First Python"
        },
        {
            "author": "Allen B. Downey",
            "title": "Think Python: How to Think Like a Computer Scientist"
        },
        {
            "author": "Eric Matthes",
            "title": "Python Crash Course"
        }
    ]
}

print(
    f"\nWelcome to {library['name']}!"
    f"\nHere we have collection of {len(library['books'])} books!"
    f"\nSHH! Please be quiet!"
    f"\nNo Smoking\n")

option = ""
while option != "q":
    print("Options:")
    print("1 - List all books")
    print("2 - Search for a book by title")
    print("3 - Add a book")
    print("4 - Remove a book")
    print("5 - Update a book")
    print("q - Quit")
    option = input("What would you like to do? \n")

    if option == "1":
        print("Listing all books...\n")
        for book in library['books']:
            print(f"\"{book['title']}\" by {book['author']}")
        print("")

    if option == "2":
        print("Searching for a book by title...")
        title = input('What is the title of the book?\n')

        for book in library['books']:
            if title == book['title']:
                print(f"\nTitle: {book['title']}")
                print(f"Author: {book['author']}\n")
                break
        else:
            print("\nSorry, We don't have that one!\n")

    if option == "3":
        print("Adding a book...")
        title = input("What's the title?\n")
        author = input("Who's the author?\n")
        new_book = {'title': title, 'author': author}
        library['books'].append(new_book)
        print('\nNew Book added!\n')

    if option == "4":
        print("Removing a book...")
        title = input('What is the title of the book?\n')

        for book in library['books']:
            if title == book['title']:
                library['books'].remove(book)
                print('\nBook removed!\n')
                break
        else:
            print("\nSorry, We don't have that one!\n")

    if option == "5":
        print("Updating a book...")
        title = input('\nWhat is the title of the book?\n')
        book_to_change = ''
        for book in library['books']:
            if title == book['title']:
                book_to_change = book
                break
        else:
            print("\nSorry, We don't have that one!\n")

        if book_to_change != '':
            new_title = input('\nNew Title: ')
            new_author = input('New Author: ')
            if new_title != '':
                book_to_change['title'] = new_title
            if new_author != '':
                book_to_change['author'] = new_author
            print('\nSuccessfully updated book!\n')
