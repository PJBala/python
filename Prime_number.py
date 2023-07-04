n=int(input("Enter Number: "))
if n>1:
    for i in range(2,n//2):
        print(i)
        if (n%i)==0:
            print(n, "is not prime number ")
            break
    else:
        print(n, "is prime number")