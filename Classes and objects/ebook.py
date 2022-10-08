class ebook():
    
    def __init__(self, title, author, pages_number):
        self.title= title
        self.author= author
        self.pages_number= pages_number
        self.is_open=False
        self.page_number=0
        
    def open_book(self):
        self.is_open=True
        print('ebook is open')
        
    def close_book(self):
        self.is_open=False
        print('ebook is closed')
        
    def show_status(self):
        if self.is_open:
            while self.page_number<self.pages_number:
                print(f'''ebook:
                autor: {self.author}
                title: {self.title}
                number of pages: {self.pages_number}
                current page: {self.page_number}
                ''')
                break
        
    def read_book(self):
        if self.is_open:
            self.page_number+=1
        else:
            print('open the book first')


    