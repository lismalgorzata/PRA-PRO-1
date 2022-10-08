import random
class Arrays():
    
    @staticmethod
    def create_array(number_of_array_elements, value_of_array_elements):
        array=[]
        for element in range(0, number_of_array_elements):
            array.append(value_of_array_elements)
        return array
    
    @staticmethod
    def create_array_with_random_in_range(number_of_array_elements, value_from, value_to):
        array=[]
        for element in range(0, number_of_array_elements):
            array.append(random.randint(value_from,value_to))
        return array
    
    @staticmethod
    def number_counter(array, value_from, value_to):
        count=0
        for element in array:
            if element >= value_from and element <= value_to :
                count+=1
        return count

x=Arrays.create_array_with_random_in_range(20,-7,8)
print(x)
print(Arrays.number_counter(x,-1,1))