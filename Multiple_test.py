# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 12:16:51 2023

@author: ajitw
"""

import pytest

""" there are two method to run multiple test 
    1. grouping test by substring matching
        cmd: !py.test -k <method_name> -v
                -k :use to substring match
                -v : increases the verbosity
    2. grouping by markers
        cmd: !py.test -m <marker name> 
"""
@pytest.mark.one    # adding marker
def test_method1():
    x= 5
    y=7
    assert x == y
    
@pytest.mark.two
def test_method2():
    a = 10
    b= 20
    assert a+ 10 == b
