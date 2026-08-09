stack=[]
file=open('browser_history.txt','r')
for website in file:
    stack.append(website.strip())
file.close()
print('Current website: ',stack[-1])
while len(stack)>1:
    input("Press enter to go back to previous website:")
    stack.pop()
    print("Current website:",stack[-1])
print("No more previous websites to go back to.")