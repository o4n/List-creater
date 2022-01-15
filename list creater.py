import random, ctypes, os
from colorama import init
ctypes.windll.kernel32.SetConsoleTitleW("yn list creater")


success = "[\x1b[32m+\x1b[39m]"
error = "[\x1b[31m-\x1b[39m]"
blue = "\033[1;36;40m"
white = "\033[1;37;40m"
init()

ch = "0123456789._abcdefghijklmnopqrstuvwxyz"
le = "._abcdefghijklmnopqrstuvwxyz"
 
 
def create():
    f = open("list.txt", "a+")
    username = ""
    listcount = 0
    for m in range(user_length):
        c = random.choice(ch)
        username += c
        listcount += 1
        if (listcount == user_length) and (not all(username) == int) and (username[0] not in ".") and \
                (username[-1] not in "."):
            f.write(username)
            f.write("\n")
            username = ""
            listcount = 0
        else:
            continue
    f.close()
 
 
def guess_letter(userscount):
    user_count = 0
    while user_count != userscount:
        for user in range(userscount):
            create()
            user_count += 1

    print ("")
    print ("{} list completed.".format(success))
    input ("press any key to exit.")
    os._exit(0)
 
print ("")
print ("          {}yn list creater{}".format(blue, white))
print ("")
user_length = abs(int(input("amount of characters: ")))
num_of_users = abs(int(input("amount to create: ")))
if user_length <= 30:
    guess_letter(num_of_users)
else:
    print ("")
    print ("{} error\nkeep # of characters below 30.".format(error)) 
    input ("press any key to exit.")
    os._exit(0)

