'''
Date: 06.09.2024
Author: Avinash Singh
Title: Create a list of integers and perform arithmetic operations between the two lists, Further, create a list
having atleast one object, integer and a string. Select any one element from this list and perform a relational
operation among other created lists.
'''

#%%

# Creating a list of Integers.
list1=[6,7,8,9,10]
list2=[1,2,3,4,5]

# Declaring lists for arithematic operations
l_add = []
l_sub = []
l_mul = []
l_div = []
l_exp = []
l_mod = []
l_fldiv = []

print(l_add,l_sub)

# Performing the arithmatic operations
for i in range(5):
    l_add.append(list1[i] + list2[i])
    l_sub.append(list1[i] - list2[i])
    l_mul.append(list1[i] * list2[i])
    l_div.append(list1[i] / list2[i])
    l_exp.append(list1[i] ** list2[i])
    l_mod.append(list1[i] % list2[i])
    l_fldiv.append(list1[i] // list2[i])
    
# Printing the Arithematic Operations
print("Addition of the two list list1 and list1 is: ", l_add)
print("Subtraction of the two list list1 and list1 is: ", l_sub)
print("Multiplication of the two list list1 and list1 is: ", l_mul)
print("Division of the two list list1 and list1 is: ", l_div)
print("Exponential of the two list list1 and list1 is: ", l_exp)
print("Modulo of the two list list1 and list1 is: ", l_mod)
print("Floor Division of the two list list1 and list1 is: ", l_fldiv)

# Creating a list with integer and string
# stu_Rec is a list containing record of student name and mark obtained
stu_Rec = [["Ram",95], ["Shyam",45], ["Rohit",12], ["Satya", 75]]

print("\nStudents who Scored less than 50: ")

for i in range(4):
    if stu_Rec[i][1] > 50:
        print(stu_Rec[i][0])




