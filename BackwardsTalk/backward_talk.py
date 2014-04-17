#!/usr/bin/env python


def revert(text):
    result = []
    for word in text.split(' '):
        revert_word = [i for i in word]
        revert_word.reverse()
        result.append(''.join(revert_word))
    return str(' '.join(result))