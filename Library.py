"""
This is a Mini Python project in which I have to created a Library
which can:

1) Take book as donation
2) lend books
3) Show Available books and its quantity
4) Show borrowed books
5) Show Donated books
6) Return Borrowed books
"""


from multiprocessing.sharedctypes import Value
from time import sleep
import pyttsx3
from threading import Thread
from time import sleep


# Main Library
class Library():
    """ 
    Hello, this is a Library
    To Show available books
    """
    objects = []
    BorrowedBooks = []
    DonatedBooks = {}

    Books = {
        "IN SEARCH OF LOST TIME": 2,
        "THE TIME MACHINE": 9,
        "HTML TO REACT": 1,
        "A TALE OF TWO CITIES": 5,
        "THE HOBBIT": 2,
        "THE LITTLE PRINCE": 3,
        "ROOM": 4,
        "THE HOLY BIBLE": 3,
        "GEETA": 4,
        "AI": 6,
        "COMPUTATIONAL THINKING": 1,
        "PROGRAMMER'S LIFE": 7,
        "GOOD OMENS": 2,
        "ALICE IN WONDERLAND": 2,
        "METRO 2033": 3,
        "METRO 2034": 4,
        "METRO 2035": 4,

    }


# Book available = True Book not availabel = False
    @staticmethod
    def BookPresent(BookName = str):
        """
        This function returns true if book is available in the library
        and false if book is not avilable in the library
        """
        if Library.Books.get(BookName) == 0:
            return False
        elif Library.Books.get(BookName) == None:
            return False
        else:
            return True
        
# Changes the no. of books left in the Library
    @classmethod
    def BookQuantity(cls,BookName = str):
        """Changes the no. of books left in the Library"""
        if Library.BookPresent(BookName) == True:
            cls.Books[BookName] -= 1
        else:
            cls.Books[BookName] = 0
            print(f"")
            line = [f"The Book '{BookName}' is not available In the Library"]
            # Audio
            AudioAndText(line,line,3.5)

# Books available in the Library  
    @classmethod
    def BooksAvailable(cls):
        """Shows which books are available with its quantity"""

        print()
        line = ["Available Books :"]
        # Audio
        AudioAndText(line,line)


        for Book,Quantity in cls.Books.items():
            line = [f"{Quantity} book of '{Book}'"]
            # Audio
            AudioAndText(line,line,2,225)
                    
# Takes only Name as input 
    def __init__(self,Name = str) -> None:
        """This is a Library it takes 2 string 1st Name and 2nd Book to be borrowed"""
        self.__class__.objects.append(self)
        self.Name = Name.split()[0].upper()

        print()
        line = [
            f"Welcome,to the Library '{self.Name}'",
            f"You are Now, An Official Member of the Library"
            ]

        AudioAndText(line,line)

# Creates a list(BorrowedBooks) of borrowed books and subtracts the quntity of book present in the Library
    def BorrowBook(self,BookName = str):
        """
        Creates a list(BorrowedBooks) of borrowed books and subtracts the quntity of book
        present in the Library
        """
        BN = BookName.strip().upper()

    # If the no of books available is not zero and person has not borrowed the book before
        if Library.BookPresent(BN) == True and (BN in self.BorrowedBooks) == False:
            self.BorrowedBooks.append(BN)
            self.BookQuantity(BN)

            print(f"")
            line = [f"You borrowed : {BN} "]
            # Audio
            AudioAndText(line,line,3)

    # If the user has already borrowed the book
        elif (BN in self.BorrowedBooks) == True:
            
            print(f"")
            line = [f"You already borrowed {BN}","Plz return the book First !!"]
            AudioAndText(line,line,2.5)

        

    # If the no of books available is zero        
        else:
            self.BookQuantity(BN)


# Prints the name of the Books borrowed by a person
    def Borrowed_Books_List(self):
        """
        Prints the name of Books of a person stored in the Library 
        does not require any inputs
        """
        if self.BorrowedBooks == []:
            print()
            line = [f"You have not borrowed any book yet !"]
            # Audio
            AudioAndText(line,line)
        
        else:
            print()
            
            # Text
            line = [f"{self.Name} Library:"]
            # Audio
            AudioAndText(line,line,2)

            # list of borrowed book
            AudioAndText(self.BorrowedBooks,self.BorrowedBooks,1.5)

    

# Returning the Book
    def ReturnBook(self,BookName = str):
        """
        Prints the name of Books of a person stored in the Library
        requires name of the book in string
        """
        BookName = BookName.upper()
        try:
            del self.BorrowedBooks[self.BorrowedBooks.index(BookName)]
            print()
            line = [f"The book '{BookName}' was returned successfully!!"]

            # Audio
            AudioAndText(line,line,3)
            # Adds the quantity of book
            self.__class__.Books[BookName] +=1
        except:
            print()
            line = [f"You didn't borrowed '{BookName}'"]

            # Audio
            AudioAndText(line, line)


# Donating a Book
    def DonateBook(self,BookName = str,Quantity = int):
        """
        Adds book to the library
        requires "Book name" and "Quantity" as input
        """
        BN = BookName.strip().upper()
        cls = self.__class__
        self.DonatedBooks[BN] = Quantity
        try:
            cls.Books[BN] += Quantity

            print()
            l1 = [f"Thanks for your donation of {BN}!!"]
            AudioAndText(l1,l1)

            # Line is too big to print together with above line
            l2 = [f"Quantity of '{BN}' book is now increased to : {cls.Books[BN]}"]
            AudioAndText(l2,l2,4,180)
            
        except:
            cls.Books[BN] = Quantity

            print()
            l1 = [f"Thanks for your donation of {BN}!!"]
            AudioAndText(l1,l1)

            l2 = [f"Quantity of '{BN}' book is now increased to : {cls.Books[BN]}"]
            AudioAndText(l2,l2,4,180)


# Prints the list of Donated Books
    def Donated_Books_List(self):

        print()
        if len(self.DonatedBooks) != 0:
            l1 = [f"{self.Name}, You have donated :"]
            AudioAndText(l1,l1)

            for key, values in self.DonatedBooks.items():
                line = [f"{values} books of '{key}'"]
                
                AudioAndText(line,line)
        
        else:
            print()
            l2 = [f"Dear {self.Name}, You have not donated any book yet!"]
            AudioAndText(l2,l2,4,180)


# Slow printing of a list
def gap(List,GapDuration = 0.5):
    """Slowly print downs the lines of a list"""
    for i in List:
        print(f"{i}")
        sleep(GapDuration)

# Print text and play audio simultaniously
def AudioAndText(Text,Audio,PrintDelay = 3,VoiceSpeed = 150):
    """
    So this is a funcion which plays audio and print text simultaniously
    1st Input = Text can be list or a string
    2nd Audio = Audio can be list or a string
    3rd Delay = specifing time for delay in text ouput
    4th VoiceSpeed = Rate at which speaking occur
    """
        
    # function 1 for Text Output
    def TextOutput():
        gap(Text,PrintDelay)
    
    # funtion 3 for Audio Output
    def AudioOutput():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty("voice",voices[1].id)
        engine.setProperty("rate",VoiceSpeed)
        engine.say(Audio)
        engine.runAndWait()

    # specifying Task 1
    Task1 = Thread(target=TextOutput)
    Task1.start()

    # specifying tak 2
    Task2 = Thread(target=AudioOutput)
    Task2.start()

    # Adding sleep so that multi tasking doesn't crash
    sleep(len(Audio)*PrintDelay+0.5)



if __name__ =="__main__":
    
    WelcomeLines = [
        "\n\nHello, This is a Library",
        "But not just a simple Library",
        "As you are hearing this library speaks",
        "Thisss is a fully functioning Virtual Library ",
        "\t-Made by 'Krishna' ",
        "\n\nThere are many functionalities of the library, to use",
        "But First, Because I don't know what I should call you",
        "Let me know your name"
    ]
    WelcomeAudioLines = [
        "Hello, This is a Library",
        "But not just a simple Library",
        "As you are hearing this library speaks",
        "Thisss is a fully functioning Virtual Library ",
        "Made by 'Krishna' ",
        "There are many functionalities of the library, to use",
        "But First, Because I don't know what I should call you",
        "Let me know your name"

    ]

# Welcome Lines 
    AudioAndText(WelcomeLines,WelcomeAudioLines,2.5)

# User
    print()
    User = Library(input("Type your name : "))
    print()

# Print Options
    def Options():
                
        OptionLines = [

            "\n\t1) See which books are available in the Library",
            "\t2) You can borrow a book if you like",
            "\t3) Return the book after reading",
            "\t4) See which books you have borrowed",
            "\t5) Donate book for other to read",
            "\t6) See your Donated books",

        ]
        OptionAudioLines = [
            
            "1) See which books are available in the Library",
            "2) You can borrow a book if you like",
            "3) Return the book after reading",
            "4) See which books you have borrowed",
            "5) Donate book for other to read",
            "6) See your Donated books",
        ]

        AudioAndText(OptionLines,OptionAudioLines,3)


    print()

    li = [
        "Wondering, What you can do in this library",
        "There are many Options to choose from \n"
    ]
    Ai = [
        "Wondering, What you can do in this library",
        "There are many Options to choose from "
    ]

    AudioAndText(li,Ai)
# Loop
    while True:
        print()
        l = ["Type 'Yes' to show Options or 'No' to continue"]

        AudioAndText(l,l)
        print()
        Choice = input("Type 'Yes' or 'No' : ").upper()

        if Choice == 'YES' or Choice == 'Y':
            Options()
        else:
            pass

    # Options
        print(f"")
        OptionInput = ["Choose from Option 1 to 6"]

        AudioAndText(OptionInput,OptionInput,2)

        Option = input("Choose Option : ")

    # Actions according to the choosen options
        if '1'<= Option <='6':


        # Show Available Books
            if Option == '1':
                User.BooksAvailable()

        # Borrow Book
            elif Option == '2':
                print()
                # User and AI interaction
                line = [
                    f"{User.Name}, as I can see ",
                    f"You want to borrow a book",
                    ]

                AudioAndText(line,line,2.5)
                print()

                YorE = [f"Type the name of the book you want to borrow"]
                AudioAndText(YorE,YorE,1.5)

                BookName = input("Enter Book Name : ")

                User.BorrowBook(BookName)


        # Return Book
            elif Option == '3':
                print()
                line = [
                    "So, You want to return a book ",
                    "Type the name of the book"
                ]

                AudioAndText(line,line,1.5)
                BookName = input("Book Name : ")

                User.ReturnBook(BookName)        

        # List of Borrowed Books
            elif Option == '4':

                User.Borrowed_Books_List()
        

        # Donate Book
            elif Option == '5':
                print(f"")

                # Text
                line = [
                    "\nFeeling generous haa",
                    "It's our pleasure to have customers like you",
                ]
                # Audio
                la = [
                    "Feeling generous haa",
                    "It's our pleasure to have customers like you",
                ]

                AudioAndText(line,la,2.5)

                print()
                l = ["Type the name of the book and its quantity "]
                AudioAndText(l,l,1.5)

                Book = input("Book Name : ")
                Quantity = input("Quantity : ")

                print()
                User.DonateBook(Book,Quantity)

        # List of Donated Books
            elif Option == '6':
                User.Donated_Books_List()
        
        else:
            print(f"")

            # Text
            line = [
                f"\nDear {User.Name},",
                "It seems like you have choosen a wrong Option",
            ]

            # Audio
            l2 = [
                f"Dear {User.Name},",
                "It seems like you have choosen a wrong Option",
            ]

            AudioAndText(line,l2)
    
    # Continue or Exit the Programm
        print()

        # Text
        line = [
            f"So, {User.Name}",
            "Do you want to continue exploring, Or",
            "Close the Library",
        ]

        AudioAndText(line,line,2.5)
        print()

        # Audo and text printing seperate to reduce the time taken to show input
        YorE = ["Type 'Yes' to continue or press 'Enter' to Exit"]
        AudioAndText(YorE,YorE,1.5)


        print()
        CoE = input("Continue Or Exit : ").upper()

    # Loop continues
        if CoE == "Y" or CoE == "YES":
            continue
    
    # Loop brakes
        else:
            
            l = [
                f"Nice to meet you, {User.Name}",
                "Good Bye !!"
            ]
            print()
            AudioAndText(l,l,1.5)
            break
