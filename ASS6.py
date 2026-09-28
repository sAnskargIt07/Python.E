while True:
    password = input("Enter password (or type stop to exit): ")

    if password == "stop":
        break



    if (len(password) >= 8 and

      any(char.isupper() for char in password) and
      any(char.islower() for char in password) and 
      any(char.isdigit() for char in password) and 
      any(char in "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~" for char in password)):
      print("Strong Password")
    else:
      print("Weak Password")