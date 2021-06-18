from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest

def test_get_determiner():
    singular_determiners = ["the", "one"]
    for _ in range(4):
        word = get_determiner(1)
        assert word in singular_determiners
    plural_determiners = ["some", "many"]
    for _ in range(4):
        word = get_determiner(2)
        assert word in plural_determiners

def test_get_noun():
    singular_nouns = ["ball", "scooter", "grape", "monkey", "almond", "baby", "guitar", "child", "muffin", "can"]
    for _ in range(12):
        noun = get_noun(1)
        assert noun in singular_nouns
    plural_nouns = ["cattle", "apples", "cats", "bugs", "adults", "loaves", "speakers", "children", "roots", "strawberries"]
    for _ in range(12):
        noun = get_noun(2)
        assert noun in plural_nouns

def test_get_verb():
    past_verbs = ["drank", "laughed", "ran", "ate", "thought", "grew", "walked", "wrote", "crawled", "talked"]
    for _ in range(12):
        verb = get_verb(1, "past")
        assert verb in past_verbs
    singular_present_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(12):
        verb = get_verb(1, "present")
        assert verb in singular_present_verbs
    plural_present_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(12):
        verb = get_verb(2, "present")
        assert verb in plural_present_verbs
    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for _ in range(12):
        verb = get_verb(1, "future")
        assert verb in future_verbs
        
def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(30):
        preposition = get_preposition()
        assert preposition in prepositions

def test_get_prepositional_phrase():
    nouns = ["cattle", "apples", "cats", "bugs", "adults", "loaves", "speakers", "children", 
        "roots", "strawberries", "ball", "scooter", "grape", "monkey", "almond", "baby", "guitar", 
        "child", "muffin", "can"]
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    determiners = ["the", "one", "some", "many"]
    quantity = [1, 2]
    item = 2
    for _ in range(15):
        prepositional_phrase = get_prepositional_phrase(quantity, item)
        split_phrase = prepositional_phrase.split(" ")
        assert split_phrase[1] in prepositions
        assert split_phrase[2] in determiners
        assert split_phrase[3] in nouns
#Normally, the indexes of 0, 1, and 2 would be used here.
#However, I have a space included in my prepositional phrase, 
#so I have the indexes adjusted to skip over it.

pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])