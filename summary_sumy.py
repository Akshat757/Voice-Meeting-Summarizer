from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

# from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from punctuator import punctuator
import spacy

# Load the English language model

def count_sentences(text):
    nlp = spacy.load("en_core_web_sm")
    # Process the text with spaCy
    doc = nlp(text)
    # Return the number of sentences
    return len(list(doc.sents))


def generate_summary(text, language="english", sentences_count=1):
    text = punctuator(text)
    sentences_count = count_sentences(text)
    summary_ratio = 0.3  # You can adjust this ratio based on your preference
    sentences_count = max(1, int(sentences_count * summary_ratio))
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    stemmer = Stemmer(language)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(language)

    summary = ""
    for sentence in summarizer(parser.document, sentences_count):
        summary += str(sentence)

    return summary

# if __name__ == "__main__":
#     TEXT = '''
#     so let me just give you an introduction about myself I am John from college medicaps university. I have been is there since last three years. I am a third year student of BTech from branch Computer Science and what time assistant for Bipasha meetings and Caesar.I have many other hobbies like playing sports listening music travelling two various places across the country.
#     '''

#     LANGUAGE = "english"
#     SENTENCES_COUNT = 1

#     summary = generate_summary(TEXT, language=LANGUAGE, sentences_count=SENTENCES_COUNT)
#     print(summary)










# from __future__ import absolute_import
# from __future__ import division, print_function, unicode_literals

# # from sumy.parsers.html import HtmlParser
# from nltk.tokenize import sent_tokenize
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer as Summarizer
# from sumy.nlp.stemmers import Stemmer
# from sumy.utils import get_stop_words
# from punctuator import punctuator



# def generate_summary(text, language="english", sentences_count=1):
#     text = punctuator(text)

#     # Tokenize the text into sentences
#     sentences = sent_tokenize(text)

#     # Calculate the number of sentences for the summary
#     total_sentences = len(sentences)
#     print(total_sentences)
#     # Define a ratio for summary size (adjust as needed)
#     summary_ratio = 0.3  # You can adjust this ratio based on your preference
#     sentences_count = max(1, int(total_sentences * summary_ratio))
#     print(sentences_count)
#     parser = PlaintextParser.from_string(text, Tokenizer(language))
#     stemmer = Stemmer(language)

#     summarizer = Summarizer(stemmer)
#     summarizer.stop_words = get_stop_words(language)

#     summary = ""
#     for sentence in summarizer(parser.document,sentences_count):
#         summary += str(sentence)

#     return summary

# # if __name__ == "__main__":
# TEXT = '''
# so let me just give you an introduction about myself I am John from 
# college medicaps university. I have been is there since last three years. I am a third 
# year student of BTech from branch Computer Science and what time assistant for Bipasha 
# meetings and Caesar. I have many other hobbies like playing sports listening music travelling 
# two various places across the country.
# in 2018 cornell researchers built a high-powered detector that in combination with an algorithm-driven process called ptychography set a world record
# by tripling the resolution of a state-of-the-art electron microscope as successful as it was that approach had a weakness it only worked with ultrathin samples that were
# a few atoms thick anything thicker would cause the electrons to scatter in ways that could not be disentangled now a team again led by david muller the samuel b eckert
# professor of engineering has bested its own record by a factor of two with an electron microscope pixel array detector empad that incorporates even more sophisticated
# 3d reconstruction algorithms the resolution is so fine-tuned the only blurring that remains is the thermal jiggling of the atoms themselves
# '''

# #     LANGUAGE = "english"
# #     SENTENCES_COUNT = 1

# #     summary = generate_summary(TEXT, language=LANGUAGE, sentences_count=SENTENCES_COUNT)
# #     print(summary)

# generate_summary(TEXT)