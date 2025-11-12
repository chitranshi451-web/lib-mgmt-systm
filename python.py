def welcome():
    print("welcome to my library")
def run():
    print("press 1 to continue")
    print("press 2 to exit")

    a=int(input("press number to continue and exit"))
    if a==1:
          book()
             
    elif a==2:
          print("thanks for visit")
          exit()
def book():
    print("press 1 for book1: atomic habbits")
    print("press 1 for book1")
    print("press 1 for book1")
    print("press 1 for book1")

b=int(input("enter book number to continue"))
if b==1:
        print("book1:--Atomic Habbits")

        run()
elif b==2:
        print("book2--rich dad poor dad")
def main():
    while True:
        run()
        book()
main()




        
 
