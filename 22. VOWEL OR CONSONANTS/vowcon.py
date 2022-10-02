character=input()
character=character.lower()

check=character.isalpha()
if (check==False):
    print("Not an alphabet")
elif(character=='a'or character=='e' or character=='i' or character=='o' or character=='u'):
    print("Vowel")
else:
    print("Consonant")
