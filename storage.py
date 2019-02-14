#! usr/bin/python3

#storage.py - program to create and store passwords to different accounts

#type add [name] to create new account and its random password
#type get [name] to copy password to clipboard
#type remove [name] to remove an account
#type change [name] [password] to change password to an existing account
#type list to print exisiting accounts


import pyperclip, sys, random, shelve, string, re


def shelveName():
    file = shelve.open('accounts')
    return file

def nameArg():
    name = sys.argv[2]
    return name

def existError(name):
    print('The account ' + name + ' does not exist')

def checkPsw(psw):
    pswRegex = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,15}$')
    if pswRegex.search(psw):
        return 1
    print(r'''Password needs to have 8 to 15 characters and contain
            at least one small letter, one capital letter and one number''')
    return 0

def listAccount():
    file = shelveName()
    print(file.keys())    

def addAccount():
    name = nameArg()
    if not isFile(name):
        #creating new password
        psw  = ''.join(random.choice(string.hexdigits) for _ in range(15))
        writeFile(name, psw)
        print('Account added')
    else:
        print('Account with this name already exists')

def getAccount():
    name = nameArg()
    if isFile(name):
        psw = readFile(name)
        pyperclip.copy(psw)
        print('Password in the clipboard')
    else:
        existError(name)

def changeAccount():
    name = nameArg()
    newPsw = sys.argv[3]
    if isFile(name):
        if checkPsw(newPsw):
            writeFile(name, newPsw)
            print('Password changed')
    else:
        existError(name)

def removeAccount():
    name = nameArg()
    if isFile(name):
        file = shelveName()
        del file[name]
        print('Account removed')
        file.close()
    else:
        existError(name)
        
def writeFile(name, psw):
    file = shelveName()
    file[name] = psw
    file.close()

def readFile(name):
    file = shelveName()
    psw = file[name]
    file.close()
    return psw
    
def isFile(name):
    file = shelveName()
    if name in list(file.keys()):
        file.close()
        return 1
    file.close()
    return 0

if sys.argv[1].lower() == 'add' and len(sys.argv) == 3:
    addAccount()
if sys.argv[1].lower() == 'get' and len(sys.argv) == 3:
    getAccount()
if sys.argv[1].lower() == 'change' and len(sys.argv) == 4:
    changeAccount()
if sys.argv[1].lower() == 'remove' and len(sys.argv) == 3:
    removeAccount()
if sys.argv[1].lower() == 'list' and len(sys.argv) == 2:
    listAccount()
