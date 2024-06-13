import random
from mad_libs_stories import stories

def get_word(word_type):
    return input(f"Enter a(n) {word_type}: ")

words = {
    "adjective1": get_word("adjective"),
    "animal": get_word("animal"),
    "verb_past_tense1": get_word("verb (past tense)"),
    "place": get_word("place"),
    "verb1": get_word("verb"),
    "adjective2": get_word("adjective"),
    "noun1": get_word("noun"),
    "plural_noun": get_word("plural noun"),
    "adjective3": get_word("adjective"),
    "verb_ending_ing": get_word("verb (ending in -ing)"),
    "noun2": get_word("noun"),
    "adverb": get_word("adverb"),
    "adjective4": get_word("adjective"),
    "verb_past_tense2": get_word("verb (past tense)"),
    "noun3": get_word("noun")
}

selected_story = random.choice(stories).format(**words)
print("\nHere is your story:")
print(selected_story)

