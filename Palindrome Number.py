n=int(input("Enter the number:"))
s=n
rev=0
while (n>0):
    r=n%10
    rev=rev*10+r
    n=n/10
print("Reverse is :",rev)
if(rev==s):
    print("the number is palindrome:")
else:
    print("the number is not palindrome:")


