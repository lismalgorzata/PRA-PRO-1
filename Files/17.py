import shutil
shutil.copyfile('sample1.txt','copy.txt')

copy=open('copy.txt')
print(copy.read())