def sort_characters(input_word):
    char_list = list(input_word) 
    length = len(char_list)
    for i in range(length):
        for j in range(0, length - i - 1):
            if char_list[j] > char_list[j + 1]:
                char_list[j], char_list[j + 1] = char_list[j + 1], char_list[j]

    return ''.join(char_list)  
input_word = input("Enter a word: ")
sorted_word = sort_characters(input_word)  
print("The sorted word is:", sorted_word)
