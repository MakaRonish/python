y=[]
l=[]
def enter_message():
    Mode=input("Encrypt(E) and decrypt(D):")
    while True:
        if Mode.upper()=="E":
            message = input('What would you like to encrypt:')

            break
        elif Mode.upper()=="D":
            message = input('What would you like to decrypt:')

            break
        else:
            print('Enter a valid mode')
            Mode = input("Encrypt(E) and decrypt(D):")
    return message,Mode

message,Mode=enter_message()

def shift(Mode,message):
    shift_number=input('What is the shift:')
    while True:
        if int(shift_number.isdigit())==0:
            print('Invalid shift')
            shift_number = input('What is the shift:')

        else:
            print(f"('{Mode}','{message}','{shift_number}')")
            break
    return shift_number

shift_number=shift(Mode,message)

def encrypt(message,shift_number):
    encrypt_text=''
    for i in message.upper():
        l.append(ord(i))
    for i in l:
        if (i+ int(shift_number)) > 90:
            y.append(chr((i + int(shift_number))-90+64))
        elif (i+ int(shift_number)) < 90:
            y.append(chr(i+int(shift_number)))
        elif i==32:
            y.append(chr(i+int(shift_number)))



    for i in y:
        encrypt_text+=i
    print(encrypt_text)

encrypt(message,shift_number)

def decrypt(message,shift_number):
    decrypt_text = ''
    for i in message.upper():
        l.append(ord(i))
    for i in l:
        if (i + int(shift_number)) > 90:
            y.append(chr((i + int(shift_number)) - 90 + 64))
        elif (i + int(shift_number)) < 90:
            y.append(chr(i + int(shift_number)))
        elif i == 32:
            y.append(chr(i + int(shift_number)))

    for i in y:
        decrypt_text+=i
    print(decrypt_text)

def process_file():
    file=input("Enter the file name:")
    mode=input("E for encrypt and D for decrypt:")
    if file.lower()=='ronish.txt':
        with open('ronish.txt') as my_file:
            print(my_file.read())



decrypt(message,shift_number)



