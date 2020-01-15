import sqlite3
import time

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
            #return("exit")
            break

     else:
         print("User_name and Password not recognised.")
         again = input("Do you want to try again?(y/n): ")
         if again.lower() == "n":
             print("Goodbye.")
             time.sleep(1)
             #return("exit")
             break
login()            
                  

