# Date: 30.08.2024
# Author: Avinash Singh
# Title: String Operations

#%%
str1="hello"
str2="world"
str3="CAPITAL"
res_str=str1+str2
print("concatenation of str1 and str2 is ", res_str)
print("repitation of str1 is ",str1*2)
#slicing operation
print("printing ell from hello ", str1[1:4])
#using upper funcion
print("Hello in uppercase ", str1.upper())
#using lower function
print("CAPITAL in lowercase ",str3.lower())
#using replace function
print("Replacing el by 123 in hello", str1.replace("el","123"))
#split function
print("split the word by letter 'e' ",str1.split('e'))
#join function
print(str1.join(str2))
