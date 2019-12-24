try:
    file = open("user.txt", "r")
except FileNotFoundError:
    file = open("user.txt", "w+")
    user = input("inserisci nome utente:\n")
    file.write("user: " + user + "\n")
    password = input("inserisci password:\n")
    file.write("password: " + password + "\n")
finally:
    try:
        print(user)
        print(password)  
    except NameError:
        file.seek(0)
        user = file.readline()[6:]
        password = file.readline()[10:]
        print(user)
        print(password)         
    file.close()