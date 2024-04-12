'''Number1 = int(input("Enter your Number1 :"))
Number2 = int(input("Enter your Number2 :"))
Number3 = int(input("Enter your Number3 :"))
Number4 = int(input("Enter your Number4 :"))
if(Number1 > Number2 and Number1 > Number3 and Number1 > Number4):
    print("A")
elif(Number2 > Number3 and Number2 > Number4 ):
    print("B")
elif(Number3 > Number4):
    print("C")
else:
    print("D")'''
'''movies = []
mov1 = input("Enter Your 1st movie :")
mov2 = input("Enter Your 2nd movie :")
mov3 = input("Enter Your 3rd movie :")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)'''
'''lists = []
copy_list = list.copy()
copy_list.reverse()
if(copy_list == list):
    print("palindrome")
else:
    print("Not palindrome")'''
'''Grades = ["a", "s", "d", "f", "g", "a", "d", "e", "a", "c"]
Grades.sort()
print(Grades)'''
'''Grades = ["a", "s", "d", "f", "g", "a", "d", "e", "a", "c"]
Grades.sort()
print(Grades)'''
'''num = int(input("Enter Your Number:"))
factorial = 1
if(num < 0):
    print("Sorry, factorial does not negative numbers")
elif(num == 0):
    print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial*i
    print("The factorial of", num, "is",factorial)'''
'''dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture","a lists of facts and figures"]
}
print(dictionary)'''
'''subjects = {
    "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
}
print(subjects)'''
'''marks = {}
x = int(input("Enter Physics marks :"))
marks.update({"physics":x})
x = int(input("Enter chemistry marks :"))
marks.update({"chemistry":x})
x = int(input("Enter maths marks :"))
marks.update({"maths":x})
print(marks)'''
'''x = 100
while x >= 1:
    print("Hello", x)
    x -= 1'''
'''n = int(input("Enter your Number :"))'''
'''x = 1
while x <= 10:
    print(x)
    x += 1'''
    
'''nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1'''
'''nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 4
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("Found Your Number at i", i)
    else :
        print("Finding")
        i += 1'''
'''i = 1
while(i <= 5):
    print(i * " * ")
    i = i + 1'''
'''for i in range (100, 0, -1):
    print(i)'''
'''n = 5
fact = 1
i = 1
while(i <= n):
    i += 1
    fact *= i
    print("factorial  =", fact)'''
'''n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
    i +=1
    print("Factorial =", fact)'''
'''friends = ["amar", "akbar", "anthony"]
print(friends[0])
print(friends[1])
print(friends[-1])
print(friends[-2])
print(friends)'''
'''friends = ["amar", "akbar", "anthony", "john", "denmark"]
print(friends[-5:-1])'''
'''marks = ["english", 95, "chemistry", 98]
marks.append("physics")
marks.append(97)
print(marks)
print(len(marks))
marks.insert(0, "math")
marks.insert(1, 99)
print(marks)
print("math" in marks)
print(len(marks)/2)
print(len(marks))
print(marks)
i = 0
while i < len(marks):
    print(marks[i])
    print(marks[i+1])
    i = i + 2'''
'''students = ["ram", "shyam", "kishan", "radha", "radhika"]
for student in students:
    if(students == "radha"):
        break
    print(student)
    for student in students:
        if(student == "kishan"):
            continue
        print(student)'''
'''marks = (95, 98, 97, 97)#marks[0] = 98
print(marks.count(97))
print(marks.index(97))'''
'''marks = {98, 97, 95, 95}
print(marks)
for score in marks:
    print(score)'''
'''marks = {"math" : 99, "chemistry" : 98, "physics" : 97}
print(marks)
print(marks["chemistry"])
marks["biology"] = 96
print(marks)'''
'''i = 1
while(i <= 5):
    print(i)
    i = i + 1'''
'''n = 5
for i in range(1, n+1):
    for j in range(1, (i*2)-1):
        print(j, end=" ")
    print()''' #numbers print karane wala
'''i = 1
while(i <= 5):
    print(1 * "*")
    i += 1'''
'''for i in range(4):
    for j in range(i):
        print("#", end="")
    for j in range(i+1):
        print("#", end="")
    for j in range(i):
        print("#", end="")
    print()'''
'''for i in range(4):
    for j in range(i+1):
        print("#", end=" ")
    print()'''
'''for i in range(6):
    for k in range(6-i):
        print("", end="")
    for j in range(i+1):
        print("#", end="")
    print()'''
'''for i in range(0, 100, 3):
    print(i)'''
for i in range(5):
    for j in range(i-5):
        print("", end="")
    print()
    for k in range(2*i):
        print("#", end="")


    









