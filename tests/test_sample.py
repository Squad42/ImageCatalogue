# SAMPLE IMPORTs TEST
from imageCatalogue.server import *


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4
