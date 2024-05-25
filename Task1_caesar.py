def encrypt(text, shift):
    encrypt_text= ""
    for char in text:
        if char.isalpha():  # Check if the character is alphabetic
            new_shift = ord(char) + shift
            if char.islower():
                if new_shift > ord('z'):
                    new_shift -= 26
                elif new_shift < ord('a'):
                    new_shift += 26
            elif char.isupper():
                if new_shift > ord('Z'):
                    new_shift -= 26
                elif new_shift < ord('A'):
                    new_shift += 26
            encrypt_text += chr(new_shift)
        else:
            encrypt_text += char
    return encrypt_text

def decrypt(text, shift):
    return encrypt(text, -shift)

while True:
    text = input("Enter 'E' to encrypt, 'D' to decrypt, or 'Q' to quit: ")
    
    if text == 'E':     
        text = input("Enter the text to encrypt: ")
        if text.isalpha():
            print("Correct input")
        else:
            print("Invalid input")   
            break
        shift = int(input("Enter the shift value (a positive integer): "))
        encrypt_text = encrypt(text, shift)
        print("Encrypted text:", encrypt_text)
    elif text == 'D':
        text = input("Enter the text to decrypt: ")
        shift = int(input("Enter the shift value (a positive integer): "))
        decrypt_text = decrypt(text, shift)
        print("Decrypted text:", decrypt_text)
    elif text == 'Q':
        print("Exiting...")
        break
    else:
        print("Invalid choice enter from the given choice")   
