import pytest

score = [0,50,100,150,250,500,1000,pytest.param(None,marks=pytest.mark.xfail),pytest.param(-200,marks=pytest.mark.xfail),pytest.param('some_type',marks=pytest.mark.xfail)]

discounts = ['1%','3%','5%','10%','no discount']