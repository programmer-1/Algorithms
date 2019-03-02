import sys

#----------------Encryption part---------------------#
   #public key(n,e) is used for encryption
   #encryoted = ((message)*e)% n
#----------------------------------------------------#
def Encrypt(n ,e,targettext):
    j = 0
    chipertext = []
    chipher = ""
    for i in targettext:
        chipertext.append(int((targettext[j])*e) % n)
        j+=1
    print("-----------Intermediate-------------------")    
    for i in chipertext:
        chipher += (str(chr(i)))
    print(chipher)    
    return chipertext      
#-----------------------Decryption Part-----------------#
   #private key(d,n) is used for decryption
   #decrypted = ((chiper)*d)% n
#-------------------------------------------------------#
def Decrypt(n,d,encrypted):
    j = 0
    plaintext = []
    plain = ""
    for i in encrypted:
        plaintext.append(int((encrypted[j])*d) % n)
        j+=1
    for i in plaintext:
        plain += (str(chr(i)))
    print('-------------Receiver--------------------')    
    print(plain)    
    return plaintext

#-------------procedure done--------------------------------
   #get the value of first prime number and store in p
   #Get the value of second prime number and store in q
   #find n = p*q
   #totient = (p-1)*(q-1)
   #e = select relative prime between 1 to totient
   #d = (1/e)%(totient)
   #Get the message to be encrypted from the used
#-----------------------------------------------------------

p = int(input("Enter the value of P : "))#first prime number
q = int(input("Enter the value of q : "))#second prime number
n = p*q 
fi_pq = (p-1)*(q-1)
e = 7
d = (1/e)%(fi_pq)
msg = input("Enter a text to encrypt : ")
print('-------------------Sender-----------------')
print(msg)
digitaltext = [ord(c) for c in msg]
encrypted = Encrypt(n,e,digitaltext)
decrypted = Decrypt(n,d,encrypted)
