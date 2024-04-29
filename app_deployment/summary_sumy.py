from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

# from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words



def generate_summary(text, language="english", sentences_count=1):
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
#     There are various types of text summarizers, including automatic summarization and manual summarization.

#     Automatic summarization uses algorithms to analyze the text and identify the most important information, such as key sentences or phrases, to create a summary. A text summarizer is a tool that uses artificial intelligence to condense a large piece of written content into a shorter, more digestible form while preserving the original meaning and context.
    
#     This process is often powered by natural language processing (NLP) and machine learning techniques.Manual summarization, on the other hand, requires a human to manually read the text and extract the most important information, which can be a time-consuming and labor-intensive process.    
# '''

#     LANGUAGE = "english"
#     SENTENCES_COUNT = 1

#     summary = generate_summary(TEXT, language=LANGUAGE, sentences_count=SENTENCES_COUNT)
#     print(summary)