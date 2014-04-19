#!/usr/bin/env python


def revert(text):
    result = []
    for line in text.split('\n'):
        new_line = []
        for word in line.split(' '):
            revert_word = [i for i in word]
            revert_word.reverse()
            new_line.append(''.join(revert_word))
        result.append('\n'.join(new_line))
    return str('\n'.join(result))