def caesar_cipher():
    key = input("Enter cipher key: ")
    
    encrypt_decrypt = input("Would you like to Encrypt or Decrypt: ")
    if encrypt_decrypt.lower() == "encrypt":
        plain_text = input("Enter your plain text: ")
        encrypted_text = c.encrypt(plain_text)
        print("Your encrypted text is: ")
        print(encrypted_text)  
    else:
        encrypted_text = input("Enter your encrypted text: ")
        decrypted_text = c.decrypt(encrypted_text)
        print("Your decrypted text is: ")
        print(decrypted_text)

def yes_or_no():
    question = input("Hello, would you like to use this program? (Please enter 'yes' or 'no') ")

    if question.lower == "yes":
        print("Program will continue")
        caesar_cipher()

    elif question.lower == "no":
        print("Program ends")
        
    else:
        print("Please enter yes or no")
        yes_or_no()

yes_or_no()