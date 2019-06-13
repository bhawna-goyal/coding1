#!/usr/bin/python3
import os
import crypt
user = input('ENTER THE USER NAME :')
if(type(user) == str):
        os.system('useradd '+user)
        unpass=crypt.crypt('hello '+user,'123')
        os.system('passwd '+unpass)
        print('USER CREATED')
else:
        print('INVALID USER')
