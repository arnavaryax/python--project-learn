username = input("input username:")
password = input("input password:")
if (username == password):
    print("Username and password cant be same") 
elif(len(password) < 8):
    print("Password is too short")
elif ( password.count("@") == 0):
    print("add atleast one @")
else:
    print("Success: Account created!")