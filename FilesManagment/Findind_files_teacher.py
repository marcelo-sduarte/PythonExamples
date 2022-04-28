"""
File: teach12_sample.py
Author: Brother Burton

Purpose: Practice finding items in files.
"""

chosen_volume = input("Which volume of scripture would you like to learn about? ")

max_chapters = -1
book_with_max = ""

# Open the file with the information
with open("books_and_chapters.txt") as books_file:

    # Iterate through the file one line at a time
    for line in books_file:
        # Split up the line based on the ":"
        parts = line.split(":")

        # Get the book and strip off any leading/trailing whitespace
        book = parts[0].strip()

        # Get the number of chapters as an integer
        chapters = int(parts[1])

        # Get the volume of scripture and strip off any leading/trailing whitespace
        scripture = parts[2].strip()

        # Check if this belongs to the user's chosen volume:
        if scripture.lower() == chosen_volume.lower():
            # Only display and check for the max inside the body
            # of this if statement. That way we are limiting it
            # to the user's chosen volume.

            print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")

            # Check to see if this book has the most chapters we've seen so far
            if chapters > max_chapters:
                # This book is the new best one!
                max_chapters = chapters # The max chapters is now this one
                book_with_max = book # Remember the name of the book

# This is now after the loop has finished
print(f"The book with the most chapters in the {chosen_volume} is: {book_with_max}")
print(f"It has {max_chapters} chapters.")