#!/usr/bin/env python3

import re
import sys
from spellchecker import SpellChecker


def getfile(fname):
    all = ""
    with open(fname, 'r') as fd:
        for line in fd:
            s = line.replace("\n", " ")
            all += s
    return all


if __name__ == "__main__":

    spell = SpellChecker()
    #spell.word_frequency.load_text_file('/usr/share/dict/words')
    doc = getfile(sys.argv[1])
    print(spell.split_words(doc))
    misspelled = spell.split_words(doc)

    for word in misspelled:
         print(spell.correction(word))  
