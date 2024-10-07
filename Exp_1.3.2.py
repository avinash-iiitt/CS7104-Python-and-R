'''
Date: 06.09.2024
Author: Avinash Singh
Title: Create a tuple of integers and perform arithmetic operations between the two tuple, Further, create a tuple
having atleast one object, integer and a string. Select any one element from this list and perform a relational
operation among other created tuple.
'''

#%%

# Creating a tuple
tup1=(6,7,8,9,10)
tup2=(1,2,3,4,5)

# Performing arithematic operations using the tuple
print("\nAddition of tup1 and tup2:", end = ' ')
for i in range(0, len(tup1), 1):
    print(tup1[i] + tup2[i], end = ' ')
    
print("\nSubtraction of tup1 and tup2:", end = ' ')
for i in range(0, len(tup1), 1):
    print(tup1[i] - tup2[i], end = ' ')


print("\nMultiplication of tup1 and tup2:", end = ' ')
for i in range(0, len(tup1), 1):
    print(tup1[i] * tup2[i], end = ' ')

print("\nDivision of tup1 and tup2:", end = ' ')
for i in range(0, len(tup1), 1):
    print(round(tup1[i] / tup2[i], 3), end = ' ')
    
print("\nReminder of tup1 and tup2:", end = ' ')
for i in range(0, len(tup1), 1):
    print(tup1[i] % tup2[i], end = ' ')

print("\nExponential of tup1 and tup2:", end = ' ')
for i in range(0, len(tup1), 1):
    print(tup1[i] ** tup2[i], end = ' ')
    
print("\nFloor Division of tup1 and tup2:", end = ' ')
for i in range(0, len(tup1), 1):
    print(tup1[i] // tup2[i], end = ' ')
    
# Creating a tuple with integer and string
# stu_Rec is a list containing record of student name and mark obtained
stu_Rec = (("Ram",95), ("Shyam",45), ("Rohit",12), ("Satya", 75))

print("\nStudents who Scored less than 50 : ", end = '')

for i in range(4):
    if stu_Rec[i][1] > 50:
        print("{}, ".format(stu_Rec[i][0]), end = ' ')
