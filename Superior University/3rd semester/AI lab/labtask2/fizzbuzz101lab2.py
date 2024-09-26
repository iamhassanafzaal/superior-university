def fizz_buzz_check(number):
    result = ""
    
    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"
    
    return result if result else str(number)

def run_fizz_buzz(up_to):
    for i in range(1, up_to + 1):
        print(fizz_buzz_check(i))


run_fizz_buzz(15)