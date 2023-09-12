# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:08:11 2023

@author: ajitw
"""
import pytest 

def func(x):
    return x + 5

def test_method():
    assert func(4) == 9
    
# Hit the command "! pytest <file_name>.py "
