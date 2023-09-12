# Grouping test using Class
import pytest

class TestClass:
    def Test_one(self):
        x= "ram"
        assert "r" in x #pass
        
    def Test_two(self):
        x= "hello"
        assert hasattr(x, "check") #fail
        
# run command !pytest grouping.py