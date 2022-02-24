N = 333759631099
e = 65537
ciphertext = 179861114548

def getPrivateExponent(e, phi):
     # Using the Extended Euclidean GCD algorithm
     d = 1 
     top1 = phi 
     top2 = phi
     while e != 1:
        k = top1 // e 
        oldTop1 = top1 
        oldTop2 = top2 

        top1 = e 
        top2 = d 

        e = oldTop1 - k * e 
        d = oldTop2 - k * d 
        if d < 0: 
            d = d % phi 
     return d 

def decrypt(ciphertext, privateKey):
     """ Returns the decoded message Params: ciphertext - integer which contains the message privateKey - list that contains the private exponent, and the modulus [d,N] """
     d = privateKey[0]
     N = privateKey[1]

     c = int(ciphertext)
     m = str(pow(c,d,N))

     if len(m) % 3 != 0:
        m = "0" + str(m)

     message = ""

     for i in range(0, len(m), 3):
        ch = m[i:i+3]
        ch = chr(int(ch))

        message += ch
     
     return message

print("\n-----------------------------------\n")

print("Welcome to the RSA Decoder!")
print("\n-----------------------------------\n")
print("Public Information - ")
print("Modulus (N) : ", N)
print("Public Exponent (e): ", e)
print("Ciphertext : ", ciphertext)
print("\nUsing this information, \nfind phi and enter its value below. If it is correct, \nthen you will get the secret message. \nAll the best\n")


while True:
    phi = int(input("\nEnter the value of phi: "))
    
    d = getPrivateExponent(e, phi)
    
    plaintext = decrypt(ciphertext, [d,N])
    print("Plaintext: ", plaintext)
    
    choice = input("Try again? [Y/n]: ")
    if choice == "n" or choice == "N":
        break

print("\nTerminating decoder...")