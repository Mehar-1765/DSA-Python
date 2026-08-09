#1)check the parenthses are balanced or not
#2)balance the unbalanced parentheses 
#3)remove the unbalanced parentheses

#check the expression is balanced or not
# expression=input('Enter expresssion: ')
# stack=[]
# balanced =True
# for ch in expression:
#     if ch in '({[':
#         stack.append(ch)
#     elif ch in ')}]':
#         if len(stack)==0:
#             balanced=False
#             break
#         top=stack.pop()
#         if (ch==')' and top!='(' or ch=='}' and top!='{' or ch==']' and top!='['):
#             balanced=False
# if len(stack)!=0:
#     balanced=False
# if balanced:
#     print('Paranthesis is balanced')
# else:
#     print('Paranthesis is unbalanced')

# balance the unbalanced parentheses 
# 1
# expression=input("Enter an expression: ")
# stack=[]
# result=""
# for ch in expression:
#     if ch == '(':
#         stack.append(ch)
#         result+=ch
#     elif ch == ')':
#         if stack:
#             stack.pop()
#             result+=ch
#         else:
#             result+='('+')'
#     else:
#         result+=ch
# while stack:
#     stack.pop()
#     result+=')'
# print("Balanced expression:", result)

# 2
# expression=input("Enter an expression: ")
# stack=[]
# result=""
# prefix=''
# for ch in expression:
#     if ch == '(':
#         stack.append(ch)
#         result+=ch
#     elif ch == ')':
#         if stack:
#             stack.pop()
#         else:
#             prefix+='('
#         result+=ch
#     else:
#         result+=ch
# while stack:
#     stack.pop()
#     result+=')'
# print("Balanced expression:",prefix+result)

# expression=input("Enter an expression: ")
# stack=[]
# result=""
# prefix=''
# for ch in expression:
#     if ch == '(':
#         stack.append(ch)
#         result+=ch
#     elif ch == ')':
#         if stack:
#             stack.pop()
#         else:
#             prefix+='('
#         result+=ch
#     else:
#         result+=ch
# while stack:
#     stack.pop()
#     result+=')'
# print("Balanced expression:",prefix+result)


# exp = input("Enter expression: ")

# # Count parentheses
# open_count = exp.count('(')
# close_count = exp.count(')')

# if close_count > open_count:

#     # Find the last + or -
#     pos = -1
#     for i in range(len(exp)-1, -1, -1):
#         if exp[i] == '+' or exp[i] == '-':
#             pos = i
#             break

#     if pos != -1:

#         # Find the previous operator or '('
#         j = pos - 1
#         while j >= 0 and exp[j] not in "+-*/(":
#             j -= 1

#         # Insert '(' after previous operator
#         exp = exp[:j+1] + '(' + exp[j+1:]

#         # Remove one extra ')' from the end
#         exp = exp[:-1]

#         print("Balanced Expression:", exp)
# else:
#     print("Expression:", exp)