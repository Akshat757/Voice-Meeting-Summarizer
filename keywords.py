from collections import Counter
import re

def is_valid_word(word):
    # Define a list of articles, prepositions, pronouns, and punctuations
    invalid_words = ["a", "an", "the", "and", "or", "but", "for", "of", "in", "on", "at", "to", "with", "by", "as", "I", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them", ",", ".", "!", "?", ";", ":", "'", '"', "have", "has", "are", "that", "this", "from", "is", "so"]
    
    # Check if the word is not in the list of invalid words and contains only alphabetic characters
    return word.lower() not in invalid_words and re.match("^[a-zA-Z]+$", word)

def top_frequent_words(text):
    # Split the text into words
    words = text.split()

    # Count the frequency of each word using Counter
    word_counts = Counter(words)

    # Get the top frequent words
    top_words = [word for word, _ in word_counts.most_common()]

    # Filter out invalid words
    valid_top_words = [word for word in top_words if is_valid_word(word)]

    # Take the top valid words
    top = valid_top_words[:5]

    # Join the words into a comma-separated sentence
    sentence = ", ".join(top)

    return sentence


# text = '''Demonstrators on Sunday breached a security barrier meant to keep opposing protest groups apart on the UCLA campus, and the two sides have come face-to-face, at times screaming at one another and shoving back and forth.

# A CNN team is on the ground watching the crowd, where pro-Palestinian demonstrators have gathered to support an encampment protesting Israel's military campaign in Gaza, and a group of counter-protesters draped in Israeli flags has erected a video screen and speaker set-up.

# “Very high passions on both sides, and when these two come together we have seen confrontations,” CNN’s Camila Bernal reported from the campus. “People who are screaming at each other, sometimes shoving and pushing, and it does get violent at times.”

# Organizers from each group have told Bernal that they are trying to keep the peace.

# The CNN team has seen police officers in riot gear standing at a distance from the crowd, but university officials have said police will not intervene unless they feel students are in harm’s way.

# The school’s vice chancellor for strategic communications, Mary Osako, confirmed in a statement that demonstrators had “breached” a barrier between the groups, and that there were “physical altercations” between protesters.

# “UCLA has a long history of being a place of peaceful protest, and we are heartbroken about the violence that broke out,” the statement reads.

# Information about any potential injuries has not been made available.'''

# top_words_sentence = top_frequent_words(text)
# print("Top 10 frequent words as a sentence:")
# print(top_words_sentence)