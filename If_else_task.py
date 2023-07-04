#python program for add two number
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
sum=a+b
print("Your total is", sum)

#Maximum of two numbers in Python
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
if a>b:
    print(a,"is maximum number")
else:
    print(b, "is maximun number")
    
#Python Program for factorial of a number
a=int(input("Enter a number:"))
for i in range(1,a):
    a=a*i
print(a)

#Python Program for simple interest & monthly installment
p=int(input("Enter the principle amount: "))
n=int(input("Enter duration of loan (in year): "))
r=12
si=(p*n*r)/100
print("your simple interest is", si)
print("monthly interest is", si/12)
mi=(p+si)/(n*12)
print("Your monthly installment is", mi)

#Python Program for compound interest
p=int(input("Enter the principle amount: "))
n=int(input("Enter duration of loan (in year): "))
r=12
amount = p*(1+r/100)**n
print(amount)
ci=amount-p
print("your compund interest is", ci)
print("Your monthly installment is ", amount/(n*12))

#prime number
l=int(input("Enter a lower number:"))
u=int(input("Enter a upper number:"))
for p in range (l,u+1):
    if p>1:
        for i in range (2,p):
            if (p%i)==0:
                break
        else:
            print("prime number are",p)
     
#Python Program for Program to find area of a circle
r=float(input("Enter the circle radius(in centimetre):" ))
A=(22/7)*r**2
print("The area of circle is", A,("cm^2"))

#Python Program to check Armstrong Number
n=int(input("Enter number"))
temp=n
q=0
while(n>0):
    digit=n%10
    q=q+digit**3
    n=n//10
if (temp==q):
    print("amstrong")
else:
    print("not amstrong")

#Python Program for Sum of squares of first n natural numbers
n=int(input("Enter the number"))
m=n*(n+1)*(2*n+1)/6
print(m)

#program to find the sum of squares of n natural numbers
n=int(input("Enter the natural number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i**2    
print("The sum of",n,"natural number is:",sum)


#Python Program for How to check if a given number is Fibonacci number?
n=int(input("Enter a number:"))
n1=1
n2=1
count=0
if n<0:
    print("Please enter positive numbers")
elif n==1:
    print("Fibonacci series of ",n, "is", n1)
else:
    while count<n:
        count=n1+n2
        n1=n2
        n2=count
    if count==n:
        print(n,"is Fibonacci number")
    else:
        print(n,"is not Fibonacci number")
        
#re-enter
n=int(input("Enter a number:"))
n1=1
n2=1
count=0
chance=3
while chance>0:
    if n<0:
        print("Please enter positive numbers")
        n=int(input("Enter a number:"))
        chance=chance-1        
    elif n==1:
        print("Fibonacci series of ",n, "is", n1)
        break
    else:
        while count<n:
            count=n1+n2
            n1=n2
            n2=count
        if count==n:    
            print(n,"is Fibonacci number")
            break
        else:
            print(n,"is not Fibonacci number")
            break        
        
        
        
        
        
    
            
            
            
            
            
            
            