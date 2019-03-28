from interpreter import *

def testGetStack():
    assert getStack([], 0) == []
    assert getStack([1,[2]], 1) == [2]
    assert getStack([[2],1], 1) == None

def testGetDepth():
    assert getDepth([]) == 0
    assert getDepth([1]) == 0
    assert getDepth([[],0]) == 0
    assert getDepth([0,[]]) == 1