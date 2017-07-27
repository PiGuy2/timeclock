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
    print()
    # ==========
    while True:
        fN = input("\tEnter your first name ==> ").lower()
        if len(fN) > 1:
            if " " not in fN:
                break
            else:
                print("\tName cannot contain spaces")
        else:
            print("\tName must be at least two letters")
    print()
    # ==========
    while True:
        mI = input("\tEnter your middle initial ==> ").lower()
        if len(mI) == 1:
            break
        elif nI == " ":
            print("\tInitial cannot be a space")
        else:
            print("\tPlease enter one letter")
    print()
    # ==========
    while True:
        lN = input("\tEnter your last name ==> ").lower()
        if len(lN) > 1:
            if " " not in lN:
                break
            else:
                print("\tName cannot contain spaces")
        else:
            print("\tName must be at least two letters")
    print()
    # ==========
    uN = input("\tEnter a username (not case sensitive) ==> ").lower()


def checkIfUserName():
    return True


def main():
    name = ""
    while True:
        inpt = input("Enter your username or a command. Type 'help' for help. ==> ").lower()
        if len(inpt) < 3:
            # too short to be a username
            print("Invalid input")
        elif inpt == "help":
            # help
            pass
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
