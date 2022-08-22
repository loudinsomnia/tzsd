import pytest
from src.scores import score
from utils.test_class import DiscountChecker


@pytest.mark.parametrize("score",score)
def test_discount(score):
    DiscountChecker().discount_checker(score=score)

