#!/usr/bin/env python
import re


def revert(text):
    result = []
    for word, space in re.findall(r'([^\s]*)(\s*)', text):
        result.append(''.join([i for i in reversed(word)]))
        result.append(space)
    return str(''.join(result))