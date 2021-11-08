import os
import sys
import inspect
# import pytest

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from exo_test import my_sort

def test_my_sort():
    assert my_sort([3,4,1,2,1]) == [1,1,2,3,4]
    assert my_sort([3,2,5,3]) == [2,3,3,5]
    assert my_sort([3.5, 2.9 , 2.5, 3.9]) == [2.5, 2.9, 3.5, 3.9]
    assert my_sort([1.5, 5, 8, 2.2]) == "ERROR: Elements should be of the same type"
    assert my_sort(['1.5', 5, 8, 2.2]) == "ERROR: Elements should be of the same type"
    assert my_sort(['g', 5, 8, 2.2]) == "ERROR: Elements should be of the same type"
    assert my_sort([True, False, True, False]) == [False, False, True,True]
    assert my_sort([3, True, 5, 3]) == "ERROR: Elements should be of the same type"