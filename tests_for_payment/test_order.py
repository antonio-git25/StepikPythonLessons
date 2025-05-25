import pytest


@pytest.mark.run(order=2)
def test_method_1():
    print("method 1")

@pytest.mark.run(order=1)
def test_method_2():
    print("method 2")

@pytest.mark.run(order=6)
def test_method_3():
    print("method 3")

@pytest.mark.run(order=4)
def test_method_4():
    print("method 4")

@pytest.mark.run(order=3)
def test_method_5():
    print("method 5")

@pytest.mark.run(order=5)
def test_method_6():
    print("method 6")

