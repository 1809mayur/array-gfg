# using stack implementation by python list we reversed the input string.

s = str(input())  # input string 
n = len(s)   # length of string
stack = [] # initialised stack

for i in s:    # appending all the element of string into stack.
    stack.append(i) 

new = str()
for i in range(n):     # reversing the string and assinging to new string by pop operation.
    new += stack.pop()

print(new)
