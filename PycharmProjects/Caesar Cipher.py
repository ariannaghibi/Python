# Write a Caesar cipher function that replaces a letter with the 13th letter after it, in the alphabet.
alphabet_list = "abcdefghijklmnopqrstuvwxyz"


def encrypt(user_input):
    cipher_text = ""
    for letter in user_input:
        if letter in alphabet_list:
            new_pos = (alphabet_list.index(letter) + 13) % 26
            cipher_text += alphabet_list[new_pos]
        else:
            cipher_text += letter
    return cipher_text


user_input = input("Enter a Phrase: ").lower()
print(encrypt(user_input))
