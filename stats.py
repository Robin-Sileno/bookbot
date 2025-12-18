def number_of_words(file_as_string):
    words = file_as_string.split()
    num_of_words = len(words)
    return num_of_words
    #print(f"Found {num_of_words} total words") 
    
def count_characters(file_as_string):
    list_of_characters = {}
    #print(file_as_string)
    lower_case_character = file_as_string.lower().split()
    
    #print(lower_case_character)
    for word in lower_case_character:
        for letter in word:
            #print(letter)      
            if letter in list_of_characters:
                list_of_characters[letter] += 1
            else:
                list_of_characters[letter] = 1
        
    #print(list_of_characters)
    return list_of_characters
    
    
def sorting_dick(input1):  
    sorted_dick = dict(sorted(input1.items(), key=lambda item: item[1], reverse=True))
    #print(sorted_dick)
    return sorted_dick