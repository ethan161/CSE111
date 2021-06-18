positive_answer_bank = []
negative_answer_bank = []
question_bank = ["I feel that I am a person of worth, at least on an equal plane with others.", 
"I feel that I have a number of good qualities.", "All in all, I am inclined to feel that I am a failure.", 
"I am able to do things as well as most other people.", "I feel I do not have much to be proud of.", 
"I take a positive attitude toward myself.", "On the whole, I am satisfied with myself.", 
"I wish I could have more respect for myself.", "I certainly feel useless at times.", 
"At times I think I am no good at all."]

def calculate_esteem(positive_answer_bank, negative_answer_bank):
    counter = 0
    for answer in positive_answer_bank:
        if answer == "d":
            counter += 1
        elif answer == "a":
            counter += 2
        elif answer == "A":
            counter += 3
    for answer in negative_answer_bank:
        if answer == "D":
            counter += 3
        elif answer == "d":
            counter += 2
        elif answer == "a":
            counter += 1
    return (counter)
    
def question_function(question_bank):
    q_counter = 1
    print("This program is an implementation of the Rosenberg Self-Esteem Scale.")
    print("This program will show you ten statements that you could possibly")
    print("apply to yourself. Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:\n")
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.\n")
    for question in question_bank:
        print(f"{q_counter}. {question}")
        if q_counter in [1, 2, 4, 6, 7]:
            positive_answer_bank.append(input("Enter D, d, a, or A: "))
        elif q_counter in [3, 5, 8, 9, 10]:
            negative_answer_bank.append(input("Enter D, d, a, or A: "))
        q_counter += 1

def main():
    question_function(question_bank)
    score = calculate_esteem(positive_answer_bank, negative_answer_bank)
    print(f"\nYour score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.\n")

main()