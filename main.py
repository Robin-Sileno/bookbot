from stats import number_of_words, count_characters, sorting_dick

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        num_of_words = number_of_words(file_contents)
        number_of_characters = count_characters(file_contents)
        sorted_dick = sorting_dick(number_of_characters)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at: {path_to_file}....")
        print("----------- Word Count ----------")
        print(f"Found {num_of_words} total words")
        print("--------- Character Count -------")
        for character in sorted_dick:
            if character.isalpha():
                print(f"{character}: {sorted_dick[character]}")
        print("============= END ===============")
    
main()
