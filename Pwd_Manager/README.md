# Password Manager
### Video Demo:  <URL HERE>
### Description: {asswprd ,amaher a;;pwomg tp add and store credentials} that are saved into a file. The passwords are encrypted.

This program is a password manager that allows the user to add or view passwords saved in a txt file "pfile.txt". The data is stored as strings separated by |,
Domain|User|Password
The password is encrypted with the standard algorithm provided by Fernet in the cruyptography package.


The first instance of the program will generate a key to use with Fernet, saved in the file 'key.key' and also check if a file containing the encrypted password exists 'pwd.key'. If it doesn't exist, the user is prompted to generate a new master password.

After this, the main functionality of the program starts.
The user can add (a) a set of domain, username and password or they can view (v) the list of existing objects save4d in the file.

The add function is called whern the user wants to add a set of credentials. In this case after reading from input the data is written to 'pfile.txt' encrypting the password with the key used by Fernet.

The view function is instead called when the user wants to retrieve the information in the file. When this is called, the user is prompted for the master password. This is matched with the decrupted password saved in 'pwd.key'. After three consecutive unsuccessful attempts the program exits.
If the master password is entered correctly, the program prints a table with columns: Domain, Username and Password and the information underneath in plain text.

## Defined functions
There are a total of 6 funcitons beyond the main function
add() - adds one set of credentials to the password file
view() - allows the user to retrieve the stored information
write_key() - generate a new key and stores it in 'key.ley 
load_key - reads the key bfrom 'key.key'
pwd_encoder - generates a new master passwoed and saevsit in 'pwd.key' after encoding it
pwd_check - check that the user input matches the master password saved in 'pwd.key'

## Requirements
### The program requires the following python packages to run correctly:

#### tabulate:
`from tabulate import tabulate``
`
#### `cryptography`
from cryptography.fernet import Fernet

Furthermore these standard modules need to be imported and installed
`import os.path``
`import getpass``
`import sys``

