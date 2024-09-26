def validate_card_number(card_number):
    reversed_digits = [int(digit) for digit in card_number[::-1]]
    for i in range(1, len(reversed_digits), 2):
        doubled_value = reversed_digits[i] * 2
        if doubled_value > 9:
            doubled_value -= 9 
        reversed_digits[i] = doubled_value
    total_sum = sum(reversed_digits)
    return total_sum % 10 == 0
card_input = input("Enter the card number: ")
if validate_card_number(card_input):
    print("The card number is valid.")
else:
    print("The card number is invalid.")
