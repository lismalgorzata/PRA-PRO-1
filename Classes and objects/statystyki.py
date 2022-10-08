class Statistics():
    
    def __init__(self, numbers):
        self.numbers=numbers
        self.max_numb=0
        self.min_numb=0
        
    def add_number(self,number):
        self.number=number
        self.numbers.append(self.number)
             
    def display_numbers(self):
        print('Numbers: ',end='')
        print(*self.numbers, sep=', ')
        
    def greatest_numb(self):
        self.max_numb=max(self.numbers)
        
    def smallest_numb(self):
        self.min_numb=min(self.numbers)
        
    def arithmetic_mean(self):
        self.suma=0
        for i in range(0, len(self.numbers)):
            self.suma=self.suma+self.numbers[i]
        self.arithmetic_mean=(self.suma)/len(self.numbers)
        
    def median(self):
        self.n=len(self.numbers)
        while self.n > 1:
            for i in range(0, self.n-1):
                if self.numbers[i]>self.numbers[i+1]:
                    self.numbers[i], self.numbers[i+1] = self.numbers[i+1], self.numbers[i]
            self.n-=1
        self.n=len(self.numbers)
        if (self.n%2)!=0 :
            self.index=int(self.n/2)
            self.median=self.numbers[self.index]
        else:
            self.index1=int((self.n/2)-1)
            self.index2=int((self.n/2))
            self.median=(self.numbers[self.index1]+self.numbers[self.index2])/2
        
    def display_results(self):
        print(f'''Min. number: {self.min_numb}
Max. number: {self.max_numb}
Arithmetic mean: {self.arithmetic_mean}
Median: {self.median}''')
        
s=Statistics([1,2,5,6])
s.add_number(7)
s.add_number(4)
s.display_numbers()
s.greatest_numb()
s.smallest_numb()
s.arithmetic_mean()
s.median()
s.display_results()

    
    
    
    