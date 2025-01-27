def main():
    # This is to open the file and read it
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count_words(file_contents)

def count_words(book):
    #This function splits the string into a list (words[]) of each word
    #and then counts the number of words (length of the list)
    
    words = book.split()
    word_count = len(words)
    
    print()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    count_characters(book) #sends to next function


def count_characters(letters):
    #This function converts the string (the book) to all lower case (.lower())
    #then runs through each character in the string and counts each
    #and creates a dictionary (character_count) with the character and number of times it appears
       
    lower_book = letters.lower()
    character_count = {}
 
    for i in lower_book:
        if i in character_count:
            character_count[i] += 1
        else:
            character_count[i] = 1
  
    # create a list of tuples from the dictionary
    character_list = list(character_count.items())

    # remove all non-letters from the list of tuples    
    for i in range ((len(character_list) - 1), -1, -1):
        if character_list[i][0].isalpha() == False:
            del character_list[i]
    sort_list(character_list) #sends to next function


def sort_list(list):
    #Sorts the list by number of character occurrences; lambda allows for tuple referencing
    list.sort(reverse=True, key=lambda a: a[1])

    for i in range (0, len(list)):
       print(f"The '{list[i][0]}' was found {list[i][1]} times.") 
    print()
    print("--- End report ---")
       


main()