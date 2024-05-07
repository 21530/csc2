
class cipher:
    def __init__(self, shift):
        self.shift = shift
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
    def encrypt(self, text):
        result = ''
        for char in text.upper():
            if char in self.alphabet:
                index = (self.alphabet.find(char) + self.shift) % 26
                result += self.alphabet[index]
            else:
                result += char
        return result
        
    def decrypt(self, text):
        result = ''
        for char in text.upper():
            if char in self.alphabet:
                index = (self.alphabet.find(char) - self.shift) % 26
                result += self.alphabet[index]
            else:
                result += char
        return result

def caesar_cipher():
    key = input("Enter cipher key: ")
    c = cipher(int(key))

    encrypt_decrypt = input("Would you like to Encrypt or Decrypt: ")
    if encrypt_decrypt.lower() == "encrypt":
            plain_text = input("Enter your plain text: ")
            encrypted_text = c.encrypt(plain_text)
            print("Your encrypted text is: ")
            print(encrypted_text)  
        
    elif encrypt_decrypt.lower() == "decrypt":
            encrypted_text = input("Enter your encrypted text: ")
            decrypted_text = c.decrypt(encrypted_text)
            print("Your decrypted text is: ")
            print(decrypted_text)

    else:
        print("Please enter encrypt or decrypt")
        return caesar_cipher() 
               
    def yes_or_no():
            while True:
                question = input("Hello, would you like to use this program: ")

                if question.lower() == "yes":
                    import time
                    def print_text_animated(text):
                        for char in text:
                            print(char, end = "", flush = True)
                            time.sleep(0.05)
                            print_text_animated("Program will continue")
                    instructions()
                    continue
                        
                elif question.lower() == "no":
                    import time
                    def print_text_animated(text):
                        for char in text:
                            print(char, end = "", flush = True)
                            time.sleep(0.05)
                    print("Program ends")
                    break

                else:
                    print("Please enter yes or no")
                    return yes_or_no()
    yes_or_no()


    def instructions():
            while True:
                question = input("Would you like to see the instructions: ")
                if question.lower() == "yes":
                    import time
                    def print_text_animated(text):
                        for char in text:
                            print(char, end = "", flush = True)
                            time.sleep(0.05)
                            print_text_animated("Instructions: ")
                            continue
                        
                elif question.lower() == "no":
                    import time
                    def print_text_animated(text):
                        for char in text:
                            print(char, end = "", flush = True)
                            time.sleep(0.05)
                    print("Program continues")
                    break
                
                else:
                    print("Please enter yes or no")
                    return instructions()      
    instructions()