class Demo(Exception):
    pass
try:
    x=int(input("Enter a number:"))
    if x==2:
        raise Demo
except Demo:
    print("Enter any number other than 2")
else:
    print("The numebr is : ",x)
