def add(x):
    if x==1:
        return x
    else:
        return x+add(x-1)
x=int(input("Enter the last number:"))
if x<0:
    print("Enter a positive integer.")
elif x==0:
    print("Enter the number greater than 0.")
else:
    print("Sum of natural numbers=",add(x))
          
