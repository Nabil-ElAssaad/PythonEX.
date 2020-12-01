def fizz_buzz(input_number):
    if (input_number % 3 == 0) and (input_number % 5 == 0):
        return "FizzBuzz"
    if input_number % 3 == 0:
        return "Fizz"
    if input_number % 5 == 0:
        return "Buzz"
    return input_number


print(fizz_buzz(15))