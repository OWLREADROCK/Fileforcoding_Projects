class AdminLoing:
    """
      A class to represent a the login function  for the admin user.

      ...

      Attributes
      ----------
      userid : str
           user id of the admin user
      passwordId : str
           password id of the admin user
      accessADMIN : int
           askes the admin if theyy would like to access

      Methods
      -------
      adminCedCheck(self):
        checks if the user id and password input is less than 0
        if len( userid, password ) == 0 askes for reinput
        then checks if user and password is admin ( userid ) , password ( passwordid)
        if not reinput  user and passs
        if ture [  admin ( userid ) , password ( passwordid) ]
         ask admin if he wants to access the admin files
    """
    def __init__(self):
        self.userId: str = input("enter your user id") # makes the input into a string
        self.passwordId: str = input("enter your password id")
        self.filename: str = input("enter the file name")
        self.accessADMIN = int(input("{0}yes or {1}no")) #makes the list input into a interger

    def adminCedCheck(self):
        while len(self.userId) <= 0 and  len(self.passwordId) <=0 : # checks the lenn of the user input  if 0 ask the user to enter a input till true

            self.userId
            # check the lenn of the  password input if 0 ask the user to input till len higher than 0
            self.passwordId
        if self.userId != "admin" and self.passwordId != "password":

            print(self.userId)
            print(self.passwordId)
            if self.userId == "admin" and self.passwordId == "password":
                print("would you like to access the admin file")
                self.filename
                self.accessADMIN
                if self.accessADMIN == 0:
                    adminfile = open(self.filename, "r")
                    print(adminfile.read())
        elif self.userId == "admin" and self.passwordId == "password":
            print("would you like to access the admin file and enter the fiile name")
            self.filename
            self.accessADMIN
            if self.accessADMIN == 0:
                try:
                  adminfile = open(self.filename, "r")
                  print(adminfile.read())
                  adminfile.close()
                except FileNotFoundError:
                    print("file not found")
                    self.accessADMIN
                    adminfile = open(self.filename, "r")
                    print(adminfile.read())
                    adminfile.close()



#atl

class AdminLogin:
    """A class to represent the login function for the admin user.

    Attributes:
        user_id (str): The user id of the admin user.
        password (str): The password of the admin user.
        filename (str): The name of the file to be accessed.
        access_admin (str): "yes" if the admin wants to access the file, "no" otherwise.
    """

    def __init__(self):
        self.user_id = input("Enter your user id: ")
        self.password = input("Enter your password: ")
        self.filename = input("Enter the file name: ")
        self.access_admin = input("Would you like to access the admin file? (yes or no) ")

    def check_credentials(self):
        """Checks if the user id and password are valid.

        If the user id and password are not valid, asks the user to re-enter them.
        If the user id and password are valid, asks the user if they want to access the admin file.
        """
        while not self.user_id:
            self.user_id = input("Enter your user id: ")
        while not self.password:
            self.password = input("Enter your password: ")

        if self.user_id != "admin" or self.password != "password":
            print("Please enter the correct information to log in.")
            self.user_id = input("Enter your user id: ")
            self.password = input("Enter your password: ")
            if self.user_id == "admin" and self.password == "password":
                self.access_admin = input("Would you like to access the admin file? (yes or no) ")
        else:
            self.access_admin = input("Would you like to access the admin file? (yes or no) ")

    def read_file(self):
        """Reads the specified file and prints its contents.

        If the file does not exist, asks the user to enter a new file name until a valid one is entered.
        """
        while True:
            try:
                with open(self.filename, "r") as f:
                    print(f.read())
                break
            except FileNotFoundError:
                print("File not found. Please enter a valid file name.")
                self.filename = input("Enter the file name: ")


p1 = AdminLoing()
p1.adminCedCheck()


