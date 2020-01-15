import sqlite3
import time
import sys

def login():
 while True:
     User_name = input("Please enter your username: ")
     Password = input("Please enter your password: ")
     with sqlite3.connect("Shared_Power.db") as db:
         cursor = db.cursor()
     find_user = ("SELECT * FROM user WHERE User_name = ? AND Password = ?")
     cursor.execute(find_user, [(User_name),(Password)])
     results = cursor.fetchall()

     if results:
        for i in results:
            print("!welcome "+i[2])
            return("exit")
            break

     else:
         print("User_name and Password not recognised.")
         again = input("Do you want to try again?(y/n): ")
         if again.lower() == "n":
             print("Goodbye.")
             time.sleep(1)
             return("exit")
             break


def newUser():
    found = 0
    while found == 0:
        User_name = input("Please enter a username: ")
        with sqlite3.connect("Shared_Power.db") as db:
            cursor = db.cursor()
        findUser = ("SELECT * FROM user WHERE User_name = ?")
        cursor.execute(findUser,[(User_name)])

        if cursor.fetchall():
            print("User_name Taken, pleasse try again")
        else:
            found = 1
            
    First_name = input("Enter your First_name: ")
    Surname = input("Enter your Surname: ")
    Password = input("Please enter your Password: ")
    Password1 = input("Please reenter your Password: ")
    while Password != Password:
            print("Your Passswords didn't match, please try again. ")
            Password = input("Please enter your Password: ")
            Password1 = input("Please reenter your Password: ")
    insertData = '''INSERT INTO user(User_name,First_name,Surname,Password)
    VALUES(?,?,?,?)'''
    cursor.execute(insertData,[(User_name),(First_name),(Surname),(Password)])
    db.commit()


def menu():
    while True:
        print("Welcome to Shared Power:")
        menu =('''
        1 - Create New User
        2 - Login to System
        3 - Exit System\n''')
        print("Make your selection: ")
        
        userChoice = input(menu)
        
        if userChoice == "1":
            newUser()
            
        elif userChoice == "2":
             login()
             
        elif userChoice == "3":
            print("Goodbye")
            sys.exit()

        else:
            print("Command not recognised. ")


menu()            

            
    
