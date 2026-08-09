# stack applications
# 1. Using file navigation
# 2.Undo redo

text=input('Enter text: ')
file=open('notes.txt','w')
file.write(text)
file.close()
#undo -> clears the file
ch=input('Undo(y/n): ')
if ch=='y':
    file=open('notes.txt','w')
    file.write('')
    file.close()
    print('Undo done!!!!')
#redo -> text write again
ch=input('Redo(y/n): ')
if ch=='y':
    file=open('notes.txt','w')
    file.write(text)
    file.close()
    print('Redo done!!!!!!')
file=open('notes.txt','r')
print('File content: ',file.read())
file.close()