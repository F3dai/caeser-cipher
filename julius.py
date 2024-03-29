import sys

logo = """
░█████╗░░█████╗░███████╗░██████╗███████╗██████╗░  ░█████╗░██╗░░░██╗██████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗  ██╔══██╗╚██╗░██╔╝██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░█████╗░░██████╔╝  ██║░░╚═╝░╚████╔╝░██████╔╝███████║█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══╝░░██╔══██╗  ██║░░██╗░░╚██╔╝░░██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝███████╗██║░░██║  ╚█████╔╝░░░██║░░░██║░░░░░██║░░██║███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚══════╝╚═╝░░╚═╝  ░╚════╝░░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
"""

vowels = ["a", "e", "i", "o", "u"]

def menu():
    while True: # Persistance
        print("\n# Select menu item #\n")
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
                print("\n[*] The longer the cypher, the more accurate the results")
                cipher = input("[*] Enter cypher: ").lower()
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
    possibilities_dict = {}
    cum = 0
    for x in range(26):
        vowel_count = 0
        cipher = list(cipher)
        for x in range(len(cipher)):
            if cipher[x].isalpha() == True:
                if cipher[x] == "z": cipher[x] = "a" # Loop back
                else: cipher[x] = chr(ord(cipher[x]) + 1)
                if cipher[x] in vowels: # Count vowels
                    vowel_count = vowel_count + 1
        cipher = ''.join(cipher)
        cum = cum + vowel_count # cumulative vowel count
        possibilities_dict.update({cipher : vowel_count})

    # Avg Calc #
    print("\n## Most likely messages ##\n")

    final = sorted(possibilities_dict.items(), key=lambda x:x[1])
    for result in final[::-1][:5]:
        print(result[0])

            
print(logo)
while True:
    menu() # Let's goooo
