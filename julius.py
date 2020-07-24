import sys
logo = """
░█████╗░░█████╗░███████╗░██████╗███████╗██████╗░  ░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗  ██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░█████╗░░██████╔╝  ██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══╝░░██╔══██╗  ██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝███████╗██║░░██║  ╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚══════╝╚═╝░░╚═╝  ░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
"""

def menu():
    print("# Select menu item #\n")
    while True: # Persistance
        
        print("[1] Encrypt\n[2] Decrypt\n[3] Quit\n") 
        try: # Validate Menu Choice
            selection = int(input("Please enter your choice:"))
            if selection == 1: 
                shift = int(input("[*] Shift key (-26 - 26): "))
                if shift <= 26 and shift >= -26: # Validate Range
                    plaintext = input("[*] Message: ").lower()
                    encrypt(plaintext, shift)
                    break
                else: 
                    print("\n[!] Out of range\n")
                    
            if selection == 2:
                print("\n[*] The longer the cipher, the more accurate the results")
                cipher = input("[*] Enter cipher: ").lower()
                decrypt(cipher)
                break
            if selection == 3:
                sys.exit()
            else:
                print("\n[!] Out of range\n")
        except ValueError:
            print("\n[!] Invalid input\n")

def encrypt(plaintext, shift):
    plaintext = list(plaintext)
    x = 0 # count
    for thing in plaintext:
        if plaintext[x].isalpha() == True:
            plaintext[x] = chr(ord(thing) + shift)

            if ord(plaintext[x]) > 122:
                plaintext[x] = chr(ord(plaintext[x]) - 26) # loop back
            elif ord(plaintext[x]) < 97:
                plaintext[x] = chr(ord(plaintext[x]) + 26) # loop forward

        x = x + 1
    print("\n[+] "+"".join(plaintext))

def decrypt(cipher):
    timmy = {}
    cum = 0
    for x in range(26):
        vowel_count = 0
        cipher = list(cipher)
        for x in range(len(cipher)):
            if cipher[x].isalpha() == True:
                if cipher[x] == "z": cipher[x] = "a" # Loop back
                else: cipher[x] = chr(ord(cipher[x]) + 1)
                if cipher[x] == "a" or cipher[x] == "e" or cipher[x] == "i" or cipher[x] == "o" or cipher[x] =="u": # Count vowels
                    vowel_count = vowel_count + 1
        cipher = ''.join(cipher)
        cum = cum + vowel_count # cumulative vowel count
        timmy.update({cipher : vowel_count})

    # Avg Calc #
    print("\n## Most likely messages ##\n")
    avg = cum / 26
    for thing in timmy:
        if timmy[thing] > avg + (avg / 2) and len(cipher) > 4: # Upper quarter 4 + chars
            print("[+] "+thing)
        elif len(cipher) < 4: # Print all if short
            print("[+] "+thing)
            
print(logo)
while True:
    menu() # Let's goooo
