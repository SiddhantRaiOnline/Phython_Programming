#Q1.
#Maximum and minimum without built in function
def find_max_min(numbers):
    max_val=numbers[0]
    min_val=numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val
nums = list(map(int, input("Enter numbers separated by space: ").split()))
maximum, minimum = find_max_min(nums)
print("Maximum:", maximum)
print("Minimum:", minimum)

#Q2.
#Sum of cubes of positive integers smaller tahn given number
def sum_of_cubes(n):
    total=0
    for i in range(1,n):
        total+=i**3
    return total
num=int(input("Enter a positive integer: "))
print("Sum of cubes:", sum_of_cubes(num))

#Q3.
#Print 1 to n using recursion
def sum_of_cubes(n):
    total = 0
    for i in range(1, n):
        total += i ** 3
    return total
num=int(input("Enter a positive integer: "))
print("Sum of cubes:", sum_of_cubes(num))

#Q4.
#Recursive Fibonacci series upto n terms
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1)+fibonacci(n - 2)
terms = int(input("Enter number of terms: "))
for i in range(terms):
    print(fibonacci(i), end=" ")

#Q5.
#Lambda function to find volume of cone
volume_cone=lambda r,h:(1/3)*3.14*r*r*h
r=float(input("Enter radius:"))
h=float(input("Enter height:"))
print("Volume of cone:", volume_cone(r, h))

#Q6.
#Lambda function to return(max,min) from list
nums=input("Enter numbers separated by space:").split()
num=[]
for item in nums:
    num.append(int(item))
max_min=lambda lst:(max(lst),min(lst))
print("Output:", max_min(num))

#Q7.(a)
#Keyword argument
def student(name,age):
    print("Name:",name)
    print("Age:",age)
student(age=20,name="Rahul")

#Q7.(b)
#Default argument
def greet(name="Student"):
    print("Hello",name)
greet()
greet("Siddhant")

#Q7.(c)
#Variable length argument
def add_numbers(*args):
    total=0
    for num in args:
        total += num
    print("Sum:",total)
add_numbers(10,20,30,40)

#Q8.
#Checking if all dictionary values are same using lambda
data={"a":10,"b":10,"c":10}
check=lambda d:len(set(d.values()))==1
if check(data):
    print("All values are same")
else:
    print("Values are not same")

#Q9.
#Create dictionary from two lists
list1=input("Enter keys separated by space:").split()
list2=input("Enter values separated by space:").split()
dictionary={}
for i in range(len(list1)):
    dictionary[list1[i]]=list2[i]
print("Generated Dictionary:", dictionary)
