class Book():
    
    def __init__(self, title, author):
        self.title= title
        self.author= author
        self.is_open=False
        
    def open(self):
        self.is_open=True
        print('book is open')
    def close(self):
        self.is_open=False
        print('book is closed')
        
class Ebook(Book):
    def __init__(self,title,author,file_name):
        self.file_name = file_name
        super().__init__(title,author)
    def book_info(self):
        print(f'EBOOK INFO:\nTitle:\t{self.title} \nAuthor:\t{self.author} \nFile:\t{self.file_name}')
        
class Article(Book):
    def __init__(self,title,author,page_numb):
        self.page_numb =page_numb
        super().__init__(title,author)
    def book_info(self):
        print(f'ARTICLE INFO:\nTitle:\t{self.title} \nAuthor:\t{self.author} \nPage number: {self.page_numb}')
        
ebook=Ebook('Twilight','Osamu Dazai','twilight-ebook.pdf')
ebook.open()
ebook.book_info()
ebook.close()
print('\n---------------\n')
article=Article('How to be the best programmer ever forever','John Metal','23')
article.open()
article.book_info()
article.close()
