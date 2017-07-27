userFile = "./userFile.txt"


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


def checkLetter(l):
    if len(l) != 1:
        print("Check letter error")
        return False
    elif l in [" ", "(", "|", "\\", "!", "^", "=", "-", "/", ":", ",", ")"]:  # disallow: ( | \ ! ^ = - / : , )
        print("You may not use any of the following characters in your name: ( | \\ ! ^ = - / : , )")
        return False
    else:
        return True


def validName(name):
    if len(name) > 1:
        lGood = True
        for l in name:
            if checkLetter(l):
                # good
                pass  # remove?
            else:
                # bad
                lGood = False
                break
        if lGood:
            # valid name
            return True
        else:
            # invalid name
            return False
    else:
        print("\tName must be at least two letters")
        return False


def createUser():
    print()
    # ==========
    while True:
        fN = input("\tEnter your first name ==> ").lower()
        if validName(fN):
            break
    print()
    # ==========
    while True:
        mI = input("\tEnter your middle initial ==> ").lower()
        if len(mI) == 1:
            break
        elif !validName(lN):
            pass
        else:
            print("\tPlease enter one letter")
    print()
    # ==========
    while True:
        lN = input("\tEnter your last name ==> ").lower()
        if validName(lN):
            break
        else:
            print("\tName must be at least two letters")
    print()
    # ==========
    uN = input("\tEnter a username (not case sensitive) ==> ").lower()


def checkIfUserName():
    return True


def main():
    # with open(userFile, 'r') as nameFile:
    #     usernamelist = nameFile.readlines()
    #     for i in range(len(usernamelist)):
    #         usernamelist[i] = usernamelist[i].strip("\n").split("|")
    #
    # allList = ["help", "new", "quit", "admin"]
    # for name in usernamelist:
    #     allList.append(name[0])
    #     allList.append(name[1])
    # ----------
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
