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

def Add_tools():
    found = 0
    while found == 0:
        Tools_name = input("Please enter a Tools_name: ")
        with sqlite3.connect("Shared_Power.db") as db:
            cursor = db.cursor()
        findTools = ("SELECT * FROM tools WHERE Tools_name = ?")
        cursor.execute(findTools,[(Tools_name)])

        if cursor.fetchall():
            print("Tools_name Taken, pleasse try again")
        else:
            found = 1
            
    
    Tools_description= input("Enter your Tools_description: ")
    Tools_price= input("Enter your Tools_price: ")
    insertData = '''INSERT INTO tools(Tools_name,Tools_description,Tools_price)
    VALUES(?,?,?)'''
    cursor.execute(insertData,[(Tools_name),(Tools_description),(Tools_price)])
    db.commit()

def Search_tools():




with sqlite3.connect("Shared_Power.db") as db:
     cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tools(
Tools_id INTEGER PRIMARY KEY,
Tools_name VARCHAR(40) NOT NULL,
Tools_description VARCHAR(250) NOT NULL,
Tools_price DECIMAL(20) NOT NULL)
""")


db.commit()

cursor.execute("SELECT * FROM tools")
print(cursor.fetchall())
          
    
        
        
             

  

def menu():
    while True:
        print("Welcome to Shared Power:")
        menu =('''
        1 - Create New User
        2 - Login to System
        3 - Exit System\n
        4 - Add Tools
        5 - Search Tools
        6 - Hire Tools''')
        print("Make your selection: ")
        
        userChoice = input(menu)
        
        if userChoice == "1":
            newUser()
            
        elif userChoice == "2":
             login()
             
        elif userChoice == "3":
            print("Goodbye")
            sys.exit()

        elif userChoice == "4":
           Add_tools()

        elif userChoice() == "5":
           Search_tools()

        elif userChoice() == "6":
            Hire_tools()

        else:
            print("Command not recognised. ")


menu()            

            
    
