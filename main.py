from cryptography.fernet import Fernet


key = Fernet.generate_key()

print("key = ",key)

with open('filekey.key', 'wb') as filekey:
    filekey.write(key)




num = input ("Enter 1 to encrypt the helloWorld.py file :")

if(num):
    #### encrypting file

    fernet = Fernet(key)

    with open('helloWorld.py', 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open('helloWorld.py', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    print("file encrypted")
    print("you may check it manually")

num = input ("Enter 2 to decrypt the helloWorld.py file :")

if(num):
    #### decrypting file

    fernet = Fernet(key)

    with open('helloWorld.py', 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open('helloWorld.py', 'wb') as dec_file:
        dec_file.write(decrypted)

    print("file decrypted")
    print("you may check it manually")
