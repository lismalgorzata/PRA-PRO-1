class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
            
    @staticmethod
    def print_in_row(array):
        print(*array, sep=',')
        

my_array = [4,1,8,7,2]
Arrays.print_in_col(my_array)
Arrays.print_in_row(my_array)
