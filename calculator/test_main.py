from calculator.main import sum,minus,multiply,divide

def testSumFunction():
    assert sum(1,2) == 3

def testMinusFunction():
    assert minus(11,1) == 10

def testMultiplyFunction():
    assert multiply(1,5) == 5

def testDivideFunction():
    assert divide(100,10) == 10
    