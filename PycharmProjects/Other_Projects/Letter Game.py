# Write a program to replace the vowel letters with 'g' or 'G'


def vowel():
    word = input("Enter a name: ")
    translation = ""
    for letter in word:
        if letter.islower():
            if letter in "aeiou":
                translation = translation + 'g'
            else:
                translation = translation + letter
        elif letter.isupper():
            if letter in "AEIOU":
                translation = translation + 'G'
            else:
                translation = translation + letter
        else:
            translation = translation + letter
    return translation


print(vowel())



