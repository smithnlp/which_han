"""This is a tool which tries to decipher which Han dialect peculiarities are
present in any given string of non-standard Chinese text. It's intended users
are learners of Chinese who know enough of the language to know what they don't
know.

TODO:
- actual dialect-specific features such as characters and grammar patterns
- explanations
- citations
"""
# import re
# import sys


def check_yue(text):
    """See if there are Cantonese trigger-characters and/or other patterns.
    """
    pass


def check_wu(text):
    """See if there are characteristically Wu-dialect linguistic features.
    """
    pass


def check_gan(text):
    """See if there are Gan-specific features.
    """
    pass


def main():
    """Take some string of Hanzi characters submitted by the user check for
    dialect traits.
    """
    text = input("Paste some non-standard Chinese text and this program will try to decipher which Han variety it represents and explain the distinguishing features.\nYOUR TEXT: ")  # noqa
    check_yue(text)
    check_wu(text)
    check_gan(text)


if __name__ == '__main__':
    main()
