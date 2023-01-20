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
        try:
         self.accessADMIN = int(input("{0}yes or {1}no")) #makes the list input into a interger
        except ValueError:
            print("only a interger given thank you")

    def adminCedCheck(self):
        while len(self.userId) <= 0 : # checks the lenn of the user input  if 0 ask the user to enter a input till true

            self.userId
            if len(self.passwordId) <= 0: # check the lenn of the  password input if 0 ask the user to input till len higher than 0
                self.passwordId
        if self.userId != "admin" and self.passwordId != "password":

            self.userId
            self.passwordId
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



class  user_RECO:



p1 = AdminLoing()
p1.adminCedCheck()
