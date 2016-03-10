while True:
    password = input("Enter a password: ")
    if len(password) < 8:
        print("Your password needs to be more than 8 words long!")
    else:
        print("Your password seems fine to me!")