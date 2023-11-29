class Library:
    def __init__(self):
        self.library= []
       
    def add_book(self, book_title, book_auther, book_copies):
        new_book =[]
        new_book.append(book_title)
        new_book.append(book_auther)
        new_book.append(book_copies)
        self.library.append(new_book)
        
    def display_all_book(self):
        for i in self.library:
            print(f"{i[0]} by {i[1]} in {i[2]}")
            
    def Search_for_abook (self, book_title):
        x = False
        for i in self.library:
            if book_title == i[0]:
                x = True
                break
        if x:
            print (f"auther: {i[1]} and the num of it's copies is: {i[2]}")
        else:
            print ("the book not found")
            
                
L1 = Library()
L1.add_book("t1","hajer",4)
L1.add_book("t2","shahad",2)
L1.add_book("t3","badrya",3)
L1.display_all_book()
L1.Search_for_abook("t2")


#another solution:
class Library:
    def __init__(self):
        self.library= []
    def add_book(self, book_title, book_auther, book_copies):
        book = {"book_title":book_title ,"book_auther":book_auther,"book_copies":book_copies}
        self.library.append(book)
        
    def display_all_book(self):    
        for i in self.library:
            print (i)
    def Search_for_abook (self, book_title):
        for i in self.library:
            if (i["book_title"]==book_title):
                print(i["book_auther"])
                
L1 = Library()
L1.add_book("t1","hajer",4)
L1.add_book("t2","shahad",2)
L1.add_book("t3","badrya",3)
L1.display_all_book()
L1.Search_for_abook("t2")
