#!/usr/bin/env python
from BackwardsTalk.backward_talk import revert


def test_revert_word():
    assert 'looc' == revert('cool')


def test_multiple_words():
    assert 'olleH dlroW' == revert('Hello World')