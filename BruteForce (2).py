'''Program that asks to either break a hashed password or set a new hashed password, by iterating a list of strings
202202091339 --> Added special characters
202202101027 --> Removed redundant import (sys)'''

import hashlib

def hash_n_check(test_pass):
    list_hash = hashlib.sha256(test_pass.encode("utf-8")).hexdigest()
    return list_hash
#############################################################################################################################################
'''Default password '''

secret_hash = '61e52b0e8c7649faf6a931afb23ddc83cfbe2f6280f5d9dd5303dc59efd92536'
#############################################################################################################################################

#############################################################################################################################################
#Characters that will be iterated through, increasing characters significantly decreases speed due to inefficency

letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n' ,'o' ,'p' , 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N' ,'O' ,'P' , 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!','@','#','$','%','^','&','*','(',')','-','_','+','=','<','>',',','.','/','?',
           '\'','"',';',':')
#############################################################################################################################################
#This will be the list iterated, joined, hashed and compared


pass_try = ['a','a','a','a']
#############################################################################################################################################
#Main loop

while True:
#############################################################################################################################################
# Prompt to hash a new password or break an existing hash

    option = input("(1) Hash a new pass (2) break the hash\n")
#############################################################################################################################################
    if option == '1':
        new_pass = input("Please enter a new pass: ")
        if len(new_pass) == 4:
            secret_hash = hash_n_check(new_pass)
            continue
        else:
            print('password must be a-z, A-Z, 0-9')
#############################################################################################################################################
    elif option == '2':

        
        for letter in letters:
            pass_try[3] = letter
            test_pass = ("".join(pass_try))
            hashed_try = hash_n_check(test_pass)
            if hashed_try == secret_hash:
                print ("The password was ", test_pass);input('Press any key to exit')
                raise SystemExit
            else:
                for letter in letters:
                    pass_try[2] = letter
                    test_pass = ("".join(pass_try))
                    hashed_try = hash_n_check(test_pass)
                    if hashed_try == secret_hash:
                        print ("The password was ", test_pass);input('Press any key to exit')
                        raise SystemExit
                    else:
                        
                        for letter in letters:
                            pass_try[1] = letter
                            test_pass = ("".join(pass_try))
                            hashed_try = hash_n_check(test_pass)
                            if hashed_try == secret_hash:
                                print ("The password was ", test_pass);input('Press any key to exit')
                                raise SystemExit
                            
                            else:
                                
                                for letter in letters:
                                    pass_try[0] = letter
                                    test_pass = ("".join(pass_try))
                                    hashed_try = hash_n_check(test_pass)
                                    if hashed_try == secret_hash:
                                        print ("The password was ", test_pass);input('Press any key to exit')
                                        raise SystemExit
                                    else:
                                        continue

        else:
            break
