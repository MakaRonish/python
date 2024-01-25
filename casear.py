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

def encrypt(message,shift_number):
    encrypt_text=''
    for i in message.upper():
        l.append(ord(i))
    for i in l:
        if (i+ int(shift_number)) > 90:
            y.append(chr((i + int(shift_number))-90+64))#-90 is that so if the asci value goes beyond z it will bring the value to 1 and +64 so that it will bring to A
        elif (i+ int(shift_number)) <= 90:
            y.append(chr(i+int(shift_number)))
        elif i==32:
            y.append(chr(i+int(shift_number)))



    for i in y:
        encrypt_text+=i
    print(encrypt_text)


def decrypt(message,shift_number):
    decrypt_text = ''
    for i in message.upper():
        l.append(ord(i))#ord() gets the ascii value for the character
    for i in l:
        if (i - int(shift_number)) <= 64:
            y.append(chr((i - int(shift_number)) +63 - 37))
        elif (i - int(shift_number)) <= 90 and (i - int(shift_number))>=65:
            y.append(chr(i - int(shift_number)))

        elif i == 32:
            y.append(chr(i - int(shift_number)))

    for i in y:
        decrypt_text+=i
    print(decrypt_text)

def main():
    dashboard()
    message,Mode=enter_message()
    shift_number=shift(Mode,message)
    if Mode.lower()=='e':
        encrypt(message, shift_number)
    elif Mode.lower()=='d':
        decrypt(message,shift_number)
    cont=input("do you want to end or continue this y to continue:")
    while cont.lower()=='y':
        l.clear()
        y.clear()
        message, Mode = enter_message()
        shift_number = shift(Mode, message)
        if Mode.lower() == 'e':
            encrypt(message, shift_number)
        elif Mode.lower() == 'd':
            decrypt(message, shift_number)
        cont = input("do you want to end or continue this y to continue:")

def dashboard():
    print("Hello there\nWelcome to encrypt and decrypt text")

main()


#
# def process_file():
#     file=input("Enter the file name:")
#     mode=input("E for encrypt and D for decrypt:")
#     return file,mode
#
# def is_file(file):
#     while True:
#         try:
#              f= open(file)
#
#         except FileNotFoundError:
#             print("file not found")
#
#         else:
#             print(f.read())
#             break
#
#     return f
#
# def fromfile(file,mode):
#     shift_number =shift()
#     with open(file,'r') as file1:
#         filetxt=file1.read()
#         if mode =='e':
#             ftext=encrypt(message,shift_number)
#         elif mode=='d':
#             ftext=decrypt(message,shift_number)
#         return ftext
#
# def message_or_file():
#     source = input("Would you like to read from file (f) or the console (c)? ").lower()
#     while source not in ["f", "c"]:
#         print("Invalid Option")
#         source = input("Would you like to read from file (f) or the console (c)? ").lower()
#     return source.lower()
#
#


#
# def main():
#     dashboard()
#     while True:
#         file=message_or_file()
#         message,mode=enter_message()
#         if file=="f":
#             file,mode=process_file()
#             f=is_file()
#             file,mode=fromfile()
#         else:
#             message,mode=enter_message()
#             shift_number=shift()
#             if mode=='e':
#                 encrypt()
#             elif mode=="d":
#                 decrypt()
#
#
# main()











