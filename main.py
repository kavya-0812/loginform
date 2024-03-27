register_block={}
def register():
    username = input("Enter your username: ")
    while username in register_block:
        print("There already exists an user with the given username")
        username = input("Enter your username")
    password = input("Enter your password")
    email_id = input("Enter your email_id")
    roll_number = input("Enter your roll_number")
    register_block[username] = (password , email_id , roll_number)
    print("Registration Successful")
def login():
    print("Welcome to login")
    username = input("Enter your username")
    password = input("Enter your password")
    if username in register_block and register_block[username][0] == password:
        print("Login successfull")
    else:
        print("Incorrect credentials")
def display():
    print(register_block)
def main():
    while True:
        print("/n1.Register")
        print("2.Login")
        print("3.SignOut")
        print("4.Details")
        choice=input("enter your choice: ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '4':
            display()
        elif choice == '3':
            print("Thankyou Visit Again")
        else:
            print("Invalid")
if __name__=="__main__":
    main()





