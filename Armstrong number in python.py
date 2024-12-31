def is_armstrong(num):
    original_num = num
    num_digits = len(str(num))
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit ** num_digits
        num //= 10
    return original_num == sum

number = int(input("Enter a number: "))
if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
