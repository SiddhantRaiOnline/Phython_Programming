#Experiment 2:Condition statements
#Q1.
#Whether a number is divisble to 3 and 5 and both
a=float(input("Enter a number:"))
if (a%3==0) &(a%5==0):
    print("Number is divisble by both")
elif (a%3==0):
    print("Number is divisble by 3 not by 5")
elif a%5==0:
    print("Number is divisble by 5 n ot by 3")
else:
    print("Number is not divisble by 3 and 5")

#Q2.
#Whether a number is multiple of 5 or not
a=float(input("Enter a number:"))
if a%5==0:
    print("Number is a multiple of 5:")
else:
    print("Number is not a multiple of 5:")

#Q3.
#Find the greatest among two number
a=float(input("Enter a number:"))
b=float(input("Enter a number:"))
if a>b:
    print("a is greater than b:",a)
elif a<b:
    print("b is greater than a:",b)
else:
    print("Both number are same")

#Q4.
#Find greatest among three numbers;2 number are not same
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a>b and a>c:
    print("Greatest number is first:",a)
elif b>a and b>c:
    print("Greatest number is second:",b)
else:
    print("Greatest number is third:",c)

#Q5.
#Quadratic equation has real or imaginary roots
x=float(input("Enter x:"))
y=float(input("Enter y:"))
z=float(input("Enter z:"))
d=y*y-4*x*z
if d>0:
 r1=(-y+d**0.5)/(2*x)
 r2=(-y-d**0.5)/(2*x)
 print("Roots are real and distinct")
 print("Root 1:",r1)
 print("Root 2:",r2)
elif d==0:
 r=-y/(2*x)
 print("Roots are real and equal")
 print("Root:", r)
else:
 real=-b/(2*x)
 imag=(d)**0.5/(2*x)
 print("Roots are imaginary")
 print("Root 1:",real,"+",imag,"i")
 print("Root 2:",real,"-",imag,"i")

#Q6.
#A year is leap year or not
year=int(input("Enter a year:"))
if (year%400==0) or (year%4==0 and year%100!= 0):
 print(year,"is a Leap Year")
else:
 print(year,"is not a Leap Year")

#Q7.
#Next date
day=int(input("Enter day in the range 1-31:"))
month=int(input("Enter month in :"))
year=int(input("Enter year:"))
if (day<1 or day>31 or month<1 or month>12 or year<1):
    print("Invalid date")
elif (month==2 and day>29):
    print("Invalid date")
else:
        print("Valid date")
leap=False
if (year%400==0) or (year%4==0 and year%100!=0):
    leap=True
if month in (1,3,5,7,8,10,12):
    max_d=31
elif month in (4,6,9,11):
    max_d=30
else:
    if leap:
        max_d=29
    else:
        max_d=28
if day<max_d:
    day+=1
else:
    day=1
    if month<12:
        month+=1
    else:
        month=1
        year+=1
print("Next Date:")
print("day=",day,"month =",month,"year =",year)
    
#Q8.
#CGPA Calculation of 5 students
name=input("Enter Name:")
roll=input("Enter Roll Number:")
sapid=input("Enter SAP ID:")
sem=input("Enter Semester:")
year=input("Enter Year:")
course=input("Enter Course:")
m1=int(input("Enter marks in PDS: "))
m2=int(input("Enter marks in Python: "))
m3=int(input("Enter marks in Chemistry: "))
m4=int(input("Enter marks in English: "))
m5=int(input("Enter marks in Physics: "))
total=m1+m2+m3+m4+m5
percentage=total/5
cgpa=percentage/10
if cgpa<=3.4:
    grade="F"
elif cgpa<=5.0:
    grade="C+"
elif cgpa<=6.0:
    grade="B"
elif cgpa<=7.0:
    grade="B+"
elif cgpa<=8.0:
    grade="A"
elif cgpa<=9.0:
    grade="A+"
else:
    grade="O(Outstanding)"
print("Grade Sheet")
print("Name:",name,"              SAPID:",sapid)
print("Roll Number:",roll,"       Course:",course)
print("Sem:",sem,"                Year:",year)            
print("Subject: Marks")
print("PDS:",m1)
print("Python:",m2)
print("Chemistry:",m3)
print("English:",m4)
print("Physics:",m5)
print("Percentage:",percentage,"%")
print("CGPA:",(cgpa, 1))
print("Grade:",grade)

#Q9.
#Grade sheet
name=input("Enter Name:")
sapid=input("Enter SAP ID:")
sem=input("Enter Semester:")
year=input("Enter Year:")
Sub1=input("Enter Subject1 name:")
marks1=int(input("Enter the marks of Sub1"))
credit=int("Enter the credit of Sub1")
if (marks1>0 and marks1<34):
    Grade1,Score1="F",0
elif (marks1>34 and marks1<34):
    Grade1,Score1="C",4
    
