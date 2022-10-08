import random

def draw_line(elements_nr, table_block_len):
    line=(elements_nr*(table_block_len+1))+1
    for i in range (0,line):
        print('-',end='')
    print()

def draw_tab_element(number,table_block):
    numb_length=len(str(number))
    space_amount=table_block-numb_length
    print('|',end='')
    for i in range(0,space_amount):
        print(" ",end='')
    print(number,end='')

table_block=8
elements_nr=5   
draw_line(elements_nr,table_block)

for i in range(0,elements_nr):
    element=random.randint(1,1000)
    draw_tab_element(element,table_block)
    
print('|',end='')
print()
draw_line(elements_nr,table_block)