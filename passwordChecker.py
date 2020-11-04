import re

pwd = input("Enter your Password : ")
if re.search("[a-z]", pwd) and \
   re.search("[A-Z]", pwd) and \
   re.search("[!,@,#", pwd) and \
   re.search("\d", pwd):
    print("Your password is Strong!")
else:
    print("Weak password!")
