# Permutaions
# def permute(arr,path):
#     if len(path)==len(arr):
#         print(path)
#         return
#     for i in range(len(arr)):
#         if arr[i] not in path:
#             path.append(arr)
#             permute(arr,path)
#             path.pop()
# arr=input('Enter elements: ').split()
# print('Permutations: ')
# permute(arr,[])

# Combinations
def combinations(arr,c,start,path):
    if len(path)==c:
        print(path)
        return 
    for i in range(start,len(arr)):
        path.append(arr[i])
        combinations(arr,c,i+1,path)
        path.pop()
arr=input('Enter elements: ').split()
c=int(input('Enter no of combination elemnets: '))
print('combinations: ')
combinations(arr,c,0,[])