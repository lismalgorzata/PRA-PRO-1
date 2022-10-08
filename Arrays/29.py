# to check if list is subset of other
# using all()
 
# initializing list
array=[1,3,66,5,2,13]
subset_array=[12,13,3]
 
# printing original lists
print ("Original list: ",*array)
print ("Original sub list: ",*subset_array)
 
# using all() to
# check subset of list
flag = 0
if(all(x in array for x in subset_array)):
    flag = 1
     
# printing result
if (flag) :
    print ("Array is subset of other.")
else :
    print ("Array isn't subset of other.")