import pytest

import strsubset as sub 

def test_getUnmatchedIndex():
    index = sub.getUnmatchedIndex("bbtg", "bbg")
    assert index == 2

def test_getNumberOfSubset():
    sub.count = 0
    sub.getNumberOfSubset("asdbnm", "adnm", False)
    assert sub.count == 3 