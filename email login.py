import re

regex="[a-z0-9]+[\.]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
def check(email):

   if (re.search(regex,email)):
      print("mail id is correct")
   else:
      print("enter mail id is wrong")

def repass():
    re = input('reenter')

    passwords(re)

def passwords(password):
    i = len(password)
    if not (5 < (i)):
        print("password length must be greater than 5")
        repass()
    elif (18 < (i)):
        print("password must be less than 18")
        repass()
    elif not re.search('[A-Z]', password):
        print("password required atleast one upper case A-Z")
        repass()
    elif not re.search("[a-z]", password):
        print("password required atleast one lower case a-z")
        repass()
    elif not re.search("[0-9]", password):
        print("password required atleast one numeric case 0-9")
        repass()
    elif re.search("[\s]", password):
        print('there is no space between password')
        repass()
    elif not re.search("[/_&%#@]", password):
        print("password required atleat one splecal character")
        repass()
    else:
        print(F" {password} is correct")
        write()

def write():
  dic = {"username": email, "password": password}
  f =  open("D:/doc/aji.txt", "x")
  f.writelines(f" {dic} ")

def forgot():
 f2=input("choose forgotpassword or exit")
 if re.findall("[\b,forgotpassword]",f2):
    d=input("enter your verification id")
    if d==email:
     print(f"your password:{password} ")
    else:
        print("enter id is wrong")
 else:
   print("exit")
def login(button):
    if  re.search("[\b,login]",button):
        login_id=input("enter your login id")
        login_password=input("enter your password")
        class Person:
            def __init__(self, email, password):
                self.email = email
                self.password = password
        p1 = Person(login_id,login_password)
        if ((email==p1.email)&(p1.password==password)):
            print("welcome to email")
        else:
          print("wrong id")
          forgot()

    else:
     print("exit")
if __name__=="__main__":
 email=input("enter your email")
 check(email)
 password=input("enter your password")
 passwords(password)
button=input("enter login or exit")
login(button)
