def is_palindrome(number):
 # Convert the number to a string and check if it equals its reverse
 return str(number) == str(number)[::-1]
 # Input from the user
number = int(input("Enter a number to check if it's a palindrome: "))
 # Check and display the result
if is_palindrome(number):
 print(f"{number} is a palindrome.")
else:
 print(f"{number} is not a palindrome.")
