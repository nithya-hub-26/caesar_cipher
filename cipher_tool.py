print ("                                                                       ")
print ("                                                                       ")
print ("            #####################################################" )       
print ("            #                                                   #" )        
print ("            #                   Caesar Cipher tool              #" ) 
print ("            #                                                   #" )                          
print ("            #                   Cryptography Tool               #" )        
print ("            #                                                   #" )            
print ("            #                                                   #" )       
print ("            #                Author : M.Nithya Kalyani          #" )       
print ("            #                                                   #" )       
print ("            #####################################################" )       

print("                                                                   ")


print("                                           ")








from string import ascii_letters
#ascii_letters will import all the lower case and upper case alphabets


def caesar_cipher(message, key):
    s = ""
    alphabet = ascii_letters + "0123456789"
    for letter in message:
        if letter in " ~`!@#$%^&*()+_-={}|[]\:;,./<>?":
            s = s + letter
        else:
            s = s + alphabet[(alphabet.index(letter) + key) % 62]  # %62 is used to make the list cyclic
    print(s)


message = str(input("Enter the message which has to be encrypted or decrypted : "))
operation = str(input("Enter the operation whether to be encrypt or decrypt : "))
key = int(input("Enter the key value to shift the values : "))
if operation == "encrypt" or operation == "ENCRYPT" or operation == "E" or operation == "e":
    caesar_cipher(message, key)
elif operation == "decrypt" or operation == "DECRYPT" or operation == "D" or operation == "d":
    key = - key
    caesar_cipher(message, key)
else:
  print("Enter the correct operation which has to be done without any spelling error ")
