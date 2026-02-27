#Q1.
#Count capital
string=input("Enter a string: ")
count=0
for ch in string:
    if ch.isupper():
        count += 1
print("Number of capital letters:", count)

#Q2.
#Count Total Number of vowel
string=input("Enter a string: ")
vowels="aeiouAEIOU"
count=0
for ch in string:
    if ch in vowels:
        count += 1
print("Total vowels:", count)

#Q3.
#Input a sentence and print words in seperate lines
sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    print(word)

#Q4.
#Count Substring Occurence
string=input("Enter main string: ")
substring=input("Enter substring: ")
count=0
for i in range(len(string) - len(substring) + 1):
    if string[i:i+len(substring)]==substring:
        count += 1
print(count)

#Q5.
#Count Occurence of each alphabets
string=input("Enter a string: ").upper()
for ch in sorted(set(string)):
    if ch.isalpha():
        print(string.count(ch),ch)

#Q6.
#Count Number of unique words using sets
string=input("Enter a string: ").upper()
for ch in sorted(set(string)):
    if ch.isalpha():
        print(string.count(ch), ch)

#Q7.
#Set Operations with fruits
n=int(input("Enter number of fruits: "))
s1=set()
s2=set()
print("Enter fruits for set 1:")
for i in range(n):
    s1.add(input())
print("Enter fruits for set 2:")
for i in range(n):
    s2.add(input())
# a) Common fruits
print("Common fruits:",s1&s2)
# b) Only in s
print("Only in s1:", s1-s2)
# c) Count of all fruits
print("Total unique fruits:",len(s1|s2))

#Q8.
#Apply Set Operations
S1={"Red", "yellow", "orange", "blue"}
S2={"violet", "blue", "purple"}
print("Union:",S1|S2)
print("Intersection:",S1&S2)
print("Difference (S1-S2):",S1-S2)
print("Difference (S2 - S1):",S2-S1)
print("Symmetric Difference:",S1^S2)
