#example of for
n=10
for n in range (10):
    print(n)

#table
for n in range (1,11):
    print(2*n)

#sum of number
sum=0
for n in range(1,11):
    sum=sum+n
    print(sum)

#pattern
for i in range(1,6):  
    for j in range (1,i+1):  
        print(i,end="")
    print()
    
#amstrong
n=int(input("enter the number"))
s=0
r=0
tem=n
while n!=0:
    r=n%10
    s=s+r*r*r
    n=n//10
if s==tem:
    print("number is amstrong")
else:
    print("number is not amstrong")

#plaindrome
n=int(input("enter the number"))
s=0
r=0
tem=n
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
if s==tem:
    print("number is palindrome")
else:
    print("number is not palindrome")


#reverse of a number
n=int(input("enter the number = "))
s=0
r=0
tem=n
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
if s==tem:
    print(s)


#sum of number using while loop
n=int(input("enter the number"))
s=0
r=0
tem=n
while n!=0:
    r=n%10
    s=s+r
    n=n//10
print(s)
