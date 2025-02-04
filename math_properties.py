import requests

# Numbers API Link
NUMBERS_API = 'http://numbersapi.com/'


def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def is_perfect(number):
    if number < 1:
        return False

    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    
    return divisors_sum == number


def armstrong(number):
    number = abs(number)

    total = 0
    for i in list(str(number)):
        total += int(i)**len(str(number))

    if total == number:
        return True
    return False


def properties(number):
    output = []
    if armstrong(number):
        output.append('armstrong')

    if number % 2 == 0:
        output.append('even')
    else:
        output.append('odd')

    return output


def digit_sum(number):
    number = abs(number)
    
    total = 0
    for i in list(str(number)):
        total += int(i)
    return total


def fun_fact(number):
    return requests.get(f"{NUMBERS_API}{str(number)}/math?json").json().get("text")

