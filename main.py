def userBool(ms):
    msg = ms + " (y/n) ==> "
    while True:
        i = input(msg).lower()
        if i in ["y", "yes"]:
            return True
        elif i in ["n", "no"]:
            return False
        else:
            print("Invalid response. Please input 'y', 'yes', 'n', or 'no'")


def createUser():
    fN = input("\tEnter your first name ==> ").lower()
    mI = input("\tEnter your middle initial ==> ").lower()
    lN = input("\tEnter your last name ==> ").lower()
    # TODO


def main():
    name = ""
    while True:
        inpt = input("Enter your username or a command. Type 'help' for help. ==> ").lower()
        if len(inpt) < 3:
            # too short to be a username
            print("Invalid input")
        elif inpt == "new":
            print("Creating a new user")
            if userBool("\tWould you like to create a new user?"):
                createUser()
            else:
                print("Canceled")
            pass
        elif inpt == "quit":
            # quit
            break
        elif inpt == "admin":
            # admin functions
            pass
        elif checkIfUser(inpt):
            # sign in
            pass
        else:
            print("Not a valid username")
            pass
        # name = getName()
        # if io == "none":
        #     io = getIO()
        #     # ---
        # if io in ["IN", "OUT"]:
        #     today, total = recordData(name, io)
        # elif io == "Options":
        #     otherOptions()
        # elif io == "cancel":  # name="cancel"
        #     pass
        # else:
        #     print("===== error with IO function =====")


if __name__ == "__main__":
    main()
    sys.exit(0)
