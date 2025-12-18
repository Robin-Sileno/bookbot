import sys
from stats import number_of_words, count_characters, sorting_dick

def main():
    path_to_book = sys.argv[1]
    with open(path_to_book) as f:
        file_contents = f.read()
        num_of_words = number_of_words(file_contents)
        number_of_characters = count_characters(file_contents)
        sorted_dick = sorting_dick(number_of_characters)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at: {path_to_book}....")
        print("----------- Word Count ----------")
        print(f"Found {num_of_words} total words")
        print("--------- Character Count -------")
        for character in sorted_dick:
            if character.isalpha():
                print(f"{character}: {sorted_dick[character]}")
        print("============= END ===============")
    
#main()
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()
    
path_to_book = str(sys.argv[1])
