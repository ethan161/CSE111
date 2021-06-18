adjective=input("Adjective: ")
animal=input("Animal: ")
verb1=input("Verb: ")
exclamation=input("Exclamation: ")
verb2=input("Verb: ")
verb3=input("Verb: ")
noun=input("Noun: ")
verb4=input("Verb: ")
vowel= "aeiou"
if noun[0].lower() in vowel:
    article= "an"
else:
    article= "a"
print("\n--------------------")
print("Your story is:\n")
print(f'The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb1} down the hallway. \n"{exclamation.capitalize()}!" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, \nbut not before it tried to {verb3} right in front of my family. Because of this {animal}, I now have {article} {noun} that makes me want to {verb4}.')
