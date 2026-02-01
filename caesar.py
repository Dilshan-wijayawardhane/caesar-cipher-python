# A Caesar Cipher Program
import os.path

def welcome():
    print("Welcome to the Casear Cipher\nThis program encryts and decrypts text using Caesar Cipher.\n")
    return

def enter_message():
    mode = input("Would you like to encrypt(e) or decrypt(d): ")
    while mode not in ['e', 'd']:
        print("Invalid\nMode")
        mode = input("Would you like to encrypt(e) or decrypt(d): ")
    
    if mode=='e':
        message = input("What message would you like to encrypt: ").upper()
    elif mode =='d':
        message = input("What message would you like to decrypt:").upper()
    return mode, message

def encrypt(message, shift):
    encrypted_text = ""
    message = message.upper()
    
    for k in message:
        if k.isalpha():
            new = chr((ord(k) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += new
        else:
            encrypted_text += k
    
    return encrypted_text

def decrypt(message, shift):
    decrypted_text = ""
    message = message.upper()
    
    for k in message:
        if k.isalpha():
            new = chr((ord(k) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += new
        else:
            decrypted_text += k
    
    return decrypted_text

def process_file(filename, mode, shift):
    list_messages = []
    if is_file(filename):
        with open(filename, 'r') as file:
            for file_line in file:
                file_line = file_line.strip()
                if mode == 'e':
                    list_messages.append(encrypt(file_line, shift))
                elif mode == 'd':
                    list_messages.append(decrypt(file_line, shift))
    else:
        print("Invald Filename")
    
    return list_messages

def write_messages(lines):
    with open('results.txt', 'w') as file:
        for line in lines:
            file.write(line + "\n")
        print("Output written to results.txt")

def is_file(filename):
    return os.path.isfile(filename)

def message_or_file():
    mode = input("Would you like to read from file (f) or the console(c): ")
    while mode not in ['c', 'f']:
        print("Invalid \nMode\n enter  (f)for file or the console for(c)")
        mode = input("Would you like to read from file (f) or the console(c): ")

    filename = None
    message = None

    if mode == 'f':
        filename = input("Enter a filename: ").upper()
        while not is_file(filename):
            print("Invalid Filename")
            filename = input("Enter a filename: ").upper()
    
    while True:
        try:
            shift = int(input("What is shift number: "))
            if 0 <= shift <= 25:
                break
            else:
                print("Wrong shift value (must be between 0 and 25).")
        except ValueError:
            print("Input a valid number for shift.")
    
    return mode, message, filename, shift

def main():
    welcome()
    while True:
        
        mode, message, filename, shift = message_or_file()
        
        if mode == 'c':
            mode, message = enter_message()
            if mode == 'e':
                encrypted_message = encrypt(message, shift)
                print(f"ENCRYPTED output: {encrypted_message}")
            elif mode == 'd':
                decrypted_message = decrypt(message, shift)
                print(f"DECRYPTED output: {decrypted_message}")
        
        elif mode == 'f':
            file_mode = input("Would you like your file to be encrypted (e) or decrypted (d)? ")
            while file_mode not in ['e', 'd']:
                print("Invalide\nMode\Enter e for encrypt or d for decrypt\n")
                file_mode = input("Would you like your file to be encrypted (e) or decrypted (d)? ")
            
            processed_lines = process_file(filename, file_mode, shift)
            write_messages(processed_lines)


        next_time = input("Would you like to encrypt or decrypt another message? (y/n): ")

        while next_time != 'y' and next_time != 'n':
            print("Invalid input")
            next_time = input("Would you like to encrypt or decrypt another message? (y/n): ")

        if next_time.lower() != 'y':
            print("Thank you for using the program. goodbye!")
            break

if __name__ == '__main__':
    main()
