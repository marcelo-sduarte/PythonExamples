"""

12 Teach: Team Activity
Finding Items in a File

"""

with open('books_and_chapters.txt') as books:
    largest_book = 0
    name_book = ''
    for book in books:
        book = book.strip()
        book = book.split(':')
        chapters = int(book[1])
        if chapters > largest_book:
            largest_book = chapters
            name_book = book[0]
            
        print(f'Scripture: {book[2]}, Book: {book[0]}, \
            \nChapters: {book[1]}')
    print(f'The largest number of chapters is: {largest_book} \
        \nThe book that has the largest number of chapters is: {name_book} \
        \n')