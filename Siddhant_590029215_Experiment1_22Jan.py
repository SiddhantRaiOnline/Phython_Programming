#Experiment 1:Phython basics
#Q1.
#Miscellaneous(Convert degree celsius to fahrenheit and kelvin)
c=float(input("Enter temperature in Celsius: "))
f=(c*9/5)+32
k=c+273.15
print("Fahrenheit =",f)
print("Kelvin=",k)

#Q2.
#Age value as number and type
a=int(input("Enter your age:"))
print("Siddhant age is:",a)
print("The type of my age a is:",type(a))

#Q3.
#Print string
x=str("Hello")
print("The value of x is:",x)

#Q4.
#Different datatypes
a=18
b=18.18
c=True
d="Siddhant"
print(a)
print(b)
print(c)
print(d)

#Q5.
#Arthemetic expressions
x=9
y=7
z=5
print("9+7=",x+y)
print("9-7=",x-y)
print("9X7=",x*y)
print("9/7=",x/y)

#Q6.
#Height of a right angle triangle
b=float(input("Enter the base of right angle triangle:"))
p=float(input("Enter the perpendicular of right angle triangle:"))
h=(p**2+b**2)**0.5
print("The hupothenuse is:",h)

#Q7.
#How to find simple interest
p=float(input("Enter principal:"))
r=float(input("Enter rate:"))
t=float(input("Enter time:"))
s=(p*r*t)/100
print("Simple Interest =",s)

#Q8.
#Conversion of seconds into hours and minute
seconds=int(input("Enter seconds: "))
hrs=seconds//3600
mint=(seconds%3600)//60
remsec=seconds % 60
print("Hours:", hrs)
print("Minutes:", mint)
print("Seconds:", remsec)



#Q9.
#Area of triangle(Heron's formula)
a=float(input("Enter side a: "))
b=float(input("Enter side b: "))
c=float(input("Enter side c: "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c)**0.5)
print("Area of triangle=",area)


#Q10.
#Swapping 2 numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
a=a+b
b=a-b
a=a-b
print("After swapping:")
print("a=",a)
print("b=",b)

#Q11.
#Sum of N numbers
n=int(input("Enter a number: "))
sum=n*(n+1)//2
print("Sum =",sum)

#Q12.
#truth table
a=(0,1)
b=(0,1)
print("A B\A&B\A|B\A^B")
a=0
b=0
print(a,b,a&b,a|b,a^b)
a=0
b=1
print(a,b,a&b,a|b,a^b)
a=1
b=0
print(a,b,a&b,a|b,a^b)
a=1
b=1
print(a,b,a&b,a|b,a^b)

#Q13.
#Left and right shift
num=int(input("Enter a number:"))
s=int(input("Enter number of shifts:"))
print("Left shift result:",num<<s)
print("Right shift result:",num>>s)

#Q14.
#Membership operator
seq=(10,20,56,78,89)
num=int(input("Enter a number: "))
if num in seq:
    print("Number is present")
else:
    print("Not present")






    

