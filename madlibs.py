#!python3

import re

text = """
    Giraffes have aroused the curiosity of __PLURAL_NOUN__ since
    earliest times. The giraffe is the
    tallest of all living __PLURAL_NOUN__, but scientists are unable
    to explain how it got its long __PART_OF_THE_BODY__.
    The giraffe's tremendous height, which
    might reach __NUMBER__ __PLURAL_NOUN__,comes from its legs and 
    __BODYPART__.
    """

def mad_libs(mls):
    """
    :param mls: string with parts which the user should fill
    surrounded by double underscores. Underscores cannot be inside
    hit e.g., no __hint_hint__ only __hint__.
    """
    hints = re.findall("__.*?__", mls)
    if hints:
        for words in hints:
            new_word = input("enter a {} >> ".format(words))
            mls = mls.replace(words, new_word, 1)
        print ('\n')
        print (mls)
    else:
        print ("Invalid mls")

mad_libs(text)
