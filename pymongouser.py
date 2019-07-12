from pymongo import MongoClient
import getpass
import passwordRules

# Administrator log in
print("Administrator")
adminUsername = getpass.getpass("Username: ")
password = getpass.getpass()


administrator = MongoClient('192.168.99.100', 27017,
                            username=adminUsername, password=password, authMechanism='SCRAM-SHA-256')

# Administrator choose the role
# The user must observe the input however
print("Choose role:")
print("1. doctor")
print("2. researcher")
print("3. cleaner")
role = input("User's role : ")

createUser = False


doctor_database = administrator.patient
research_database = administrator.clean

# The user enters in the username and password assuming that the administrator choose the role

while not createUser and (role == "doctor" or role == "researcher" or role == "cleaner"):
    print("Now user, enter your user name and password: ")
    rules = "The following rules are:\n"
    rules += "1. the password must have length of 12 or greater\n"
    rules += "2. The password must not be equal to the username\n"
    rules += "3. the password must have at least one lower case character\n"
    rules += "4. the password must have at least one upper case character\n"
    rules += "5. the password must have at least one digit\n"
    rules += "6. do not put \"password\" in your password"
    print(rules)
    username = input("User name: ")
    user_password = getpass.getpass()
    confirm_password = getpass.getpass("Confirm Password:")
    if user_password == confirm_password and passwordRules.Rules(username, user_password).result():
        print("Confirmed!")
        if role == "doctor":
            doctor_database.command("createUser", username, pwd=user_password, roles=["readWrite"])
            print("You can both read and write on the patient database.")
        elif role == "researcher":
            research_database.command("createUser", username, pwd=user_password, roles=["read"])
            print("You can only read the clean-up database.")
        else:
            doctor_database.command("createUser", username, pwd=user_password, roles=["readNonPHI"])
            research_database.command("createUser", username, pwd=user_password, roles=["readWrite"])
            print("You can only read the patient database, except private collection")
            print("We advised you not to put the patient private information in the clean database")
            print("The main administrator have access to the clean-up database.")
            print("Any private health information (PHI) in the clean-up database will be a violation of the rules.")
            print("You can read and write the clean-up database.")
        createUser = True
    else:
        print("Try again")

