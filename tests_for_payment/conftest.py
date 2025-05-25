import pytest


@pytest.fixture()
def set_up_225():
    print("System entering is completed")
    yield
    print("exit from system")


@pytest.fixture(scope='function')
def some():
    print("Start")
    yield
    print("The End")