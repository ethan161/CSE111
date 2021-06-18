grade_percentage = float(input("What is your grade percentage? "))
if grade_percentage >= 90:
    letter = ("A")
elif 90 > grade_percentage >= 80:
    letter = ("B")
elif 80 > grade_percentage >= 70:
    letter = ("C")
elif 70 > grade_percentage >= 60:
    letter = ("D")
elif 60 > grade_percentage:
    letter = ("F")

#in this case, f isnt a vowel, but it needs the article. sue me
vowel = "af"
if letter[0].lower() in vowel:
    article = ("an")
else:
    article = ("a")

#displaying the outputs
print(f"Your final grade is {article} {letter}.")
if grade_percentage >= 70:
    print("Congratulations on passing!")
else:
    print("Better luck next time!")
