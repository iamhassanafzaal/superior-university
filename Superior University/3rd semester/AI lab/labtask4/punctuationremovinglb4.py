punctuation_marks = '''!(),-[]}{.?><@#$%^&*_+=":;/*`~'''
user_input = input("Enter a string: ")
cleaned_string = ''
for character in user_input:
    if character not in punctuation_marks:
        cleaned_string += character  

print(cleaned_string)
