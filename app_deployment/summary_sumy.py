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

if __name__ == "__main__":
    TEXT = '''
    so let me just give you an introduction about myself I am John from college medicaps university. I have been is there since last three years. I am a third year student of BTech from branch Computer Science and what time assistant for Bipasha meetings and Caesar.I have many other hobbies like playing sports listening music travelling two various places across the country.
    '''

    LANGUAGE = "english"
    SENTENCES_COUNT = 1

    summary = generate_summary(TEXT, language=LANGUAGE, sentences_count=SENTENCES_COUNT)
    print(summary)