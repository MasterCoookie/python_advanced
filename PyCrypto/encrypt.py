import os
from getpass import getpass
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def encrypt(key, filename):
    chunksize = 64 * 1024
    output_file = "(encrypted)" + filename
    file_size = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(output_file, 'wb') as outfile:
            outfile.write(file_size.encode('utf-8'))
            outfile.write(IV)

            while 1:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))
                
                outfile.write(encryptor.encrypt(chunk))

def decrypt(key, filename):
    chunksize = 64 * 1024
    output_file = filename[11:]

    with open(filename, 'rb') as infile:
        file_size = int(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(output_file, 'wb') as outfile:
            while 1:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                
                outfile.write(decryptor.decrypt(chunk))
            #gets rid of all the paddings that might have got created during encryption    
            outfile.truncate(file_size)

def get_key(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()

def main():
    choice = input("Would you like to (E)ncrypt or (D)ecrypt your file?")

    if choice == 'E':
        filename = input("File to encrypt: ")
        password = getpass("Password: ")
        encrypt(get_key(password), filename)
        print("Done.")
    elif choice == 'D':
        filename = input("File to decrypt: ")
        password = getpass("Password: ")
        decrypt(get_key(password), filename)
        print("Done.")
    else:
        print("No option selected, closing...")

if __name__ == '__main__':
    main()
