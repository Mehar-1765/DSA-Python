# n=int(input('Num: '))
# sum=0
# i=1
# for k in range(n):
#     fact=1
#     for j in range(1,i+2):
#         fact*=j
#     term=i/fact
#     print(f"Term {k+1}={i}/{i+1}!={term}")
#     sum+=term
#     i+=2
# print("Sum",sum)
# TC - O(n^2) SC - O(1)

# import math
# n=int(input('Num: '))
# sum=0
# odd=1
# even=2
# for i in range(n):
#     term=odd/math.factorial(even)
#     print(f'Term {i+1} = {odd}/{even}!={term}')
#     sum+=term
#     odd+=2
#     even+=2
# print(sum)
# TC - O(n) SC - O(1)