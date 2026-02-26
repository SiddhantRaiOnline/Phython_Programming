#Q1.
#Factorial of a given number
n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact * i
print("Factorial =",fact)

#Q2.
#Amstrong number
n=int(input("Enter number: "))
a=n//100
b=(n//10)%10
c=n%10
if a*a*a +b*b*b+c*c*c==n:
    print("Armstrong number")
else:
    print("Not Armstrong number")

#Q3.
#Fibonacci
n=int(input("Enter number of terms: "))
a=0
b=1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c=a+b
    a=b
    b=c

#Q4.
#Check Prime Number
num=int(input("Enter a number: "))
if num <= 1:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

#Q5.
#Palidrome
num = int(input("Enter a number: "))
temp = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if temp == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

#Q6.
#Sum of Digits
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print("Sum of digits =", sum)

#Q7.
#Count Number Divsible by 5 or 7
count = 0
for i in range(1, 101):
    if i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")
        count += 1
print("\nTotal numbers =", count)

#Q8.
#Lowercase to uppercase
string = input("Enter a string: ")
print("Uppercase string:", string.upper())

#Q9.
#Print table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "*", i, "=", num * i)

#Q10.
#Print pattern
n = 5
for i in range(n):
    # Numbers increasing
    for j in range(1, n - i + 1):
        print(j, end="")
    # Stars with spaces
    for j in range(i):
        print(" *", end="")
    # Numbers decreasing
    for j in range(n - i, 0, -1):
        print(j, end="")
    print()

#Q11.
#Sum of series
n = int(input("Enter value of n: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + 1/i
print("Sum of series =", sum)  
