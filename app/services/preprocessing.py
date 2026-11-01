
import re
import nltk

from nltk.corpus import stopwords

stop_words = None


def get_stop_words():
    global stop_words

    if stop_words is None:
        try:
            stop_words = set(stopwords.words('english'))
        except LookupError:
            nltk.download('stopwords', quiet=True)
            stop_words = set(stopwords.words('english'))

    return stop_words


def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z ]', '', text)

    words = text.split()

    filtered_words = [
        word for word in words
        if word not in get_stop_words()
    ]

    return " ".join(filtered_words)
