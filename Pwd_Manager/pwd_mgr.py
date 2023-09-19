from cryptography.fernet import Fernet
import os.path
import getpass
import sys
from tabulate import tabulate



def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    k_file = open("key.key", "rb")
    key= k_file.read()
    k_file.close()
    return key

def pwd_encoder(pwd_to_encrypt):
    global fer
    token = fer.encrypt(pwd_to_encrypt.encode())
    with open("pwd.key", "wb") as pwd_file:
        pwd_file.write(token)

def pwd_check(input_pwd):
    global fer
    pwd_file = open("pwd.key", "rb")
    token = pwd_file.read()
    pwd_file.close()
    decrypted_pwd = fer.decrypt(token).decode()
    if input_pwd == decrypted_pwd:
        return 1
    else:
        return 0

def add():
    global fer
    #save values from input
    domain = input("Domain name: ")
    user = input("Username: ")
    pwd = getpass.getpass("Password: ")
    with open("pfile.txt", "a") as f:
        #write values to file
        # #encrypt password
        f.write(domain + '|' + user + '|' + fer.encrypt(pwd.encode()).decode() + '\n')
        #write as csv maybe?

def view():
    #cgeck master password
    check=0
    while check<3:
        value = pwd_check(getpass.getpass("Enter Master Password: "))
        if value==1:
            break
        check+=1
    if check==3:
        sys.exit("Too many incorrect attempts, Bye!")
        
    with open("pfile.txt", "r") as f:
        elenco = list()
        for line in f.readlines():
            data = line.rstrip()
            domain, user, bytepwd = data.split('|')
            #decrypt password
            pwd = fer.decrypt(bytepwd).decode()
            #print(f"Domain: {domain}, Username: {user}, Password: {pwd}")
            elenco.append([domain,user,pwd])    
        #instead of printing I want to render these in a nive table
        print(tabulate(elenco,headers=["Domain","Username","Password"],tablefmt='grid'))


def main():
    global fer
    #define key if it doesn't exist
    if os.path.exists("key.key")==False:
        write_key()
    key = load_key()
    fer = Fernet(key)
    #define master password if it doesn't exist
    if os.path.exists("pwd.key")==False:
        input_pwd = getpass.getpass("Choose your Master Password: ")
        pwd_encoder(input_pwd)

    choice=''
    #loop until valid option is given
    while choice not in ['a','v','q']:
        choice = input("Waht would you like to do? Add (a). View (v) or Quit (q)? ").lower()
    #run over the three valid options
    if choice=='q':
        sys.exit(0)
    elif choice=='a':
        add()
    #add opens form to add password
    elif choice=='v':
        view()
    #view asks for master password and shows list

if __name__ == "__main__":
    main()

