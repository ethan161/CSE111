import random

def get_noun(quantity):
    if quantity in [1]:
        nouns = ["ball", "scooter", "grape", "monkey", "almond", 
        "baby", "guitar", "child", "muffin", "dog"]
    else:
        nouns = ["cattle", "apples", "cats", "bugs", "adults", 
        "loaves", "speakers", "children", "roots", "strawberries"]
    noun = random.choice(nouns)
    return noun

def get_determiner(quantity):
    if quantity in [1]:
        words = ["the", "one"]
    else:
        words = ["some", "many"]
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank", "laughed", "ran", "ate", "thought", "grew", 
        "walked", "wrote", "crawled", "talked"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", 
        "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", 
        "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", 
        "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    verb = random.choice(verbs)
    return verb

def get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity, item):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    if item == 1:
        prepositional_phrase = ""
    else:  
        prepositional_phrase = f" {preposition} {determiner} {noun}"
    return prepositional_phrase

def main():
    prep_check = [1, 2]
    quantities = [1, 2]
    tenses = ["past", "present", "future"]
    for item in prep_check:
        for tense in tenses:
            for quantity in quantities:
                noun = get_noun(quantity)
                determiner = get_determiner(quantity)
                verb = get_verb(quantity, tense)
                prepositional_phrase = get_prepositional_phrase(quantity, item)
                print(f"{determiner.capitalize()} {noun} {verb}{prepositional_phrase}.")

main()