import pytest
from utils.discount_counter import DiscountCount, Discount
from src.scores import discounts

class DiscountChecker:
    discount = DiscountCount()

    def discount_checker(self,score):
        if score in Discount.Discount1:
            print(self.discount.discount_counter(score))
            assert self.discount.discount_counter(score) == discounts[0], f"Wrong discount"
        elif score in Discount.Discount2:
            print(self.discount.discount_counter(score))
            assert self.discount.discount_counter(score) == discounts[1], f"Wrong discount"
        elif score in Discount.Discount3:
            print(self.discount.discount_counter(score))
            assert self.discount.discount_counter(score) == discounts[2], f"Wrong discount"
        elif score >= 500:
            print(self.discount.discount_counter(score))
            assert self.discount.discount_counter(score) == discounts[3], f"Wrong discount"
        else:
            print(self.discount.discount_counter(score))
            assert self.discount.discount_counter(score) == discounts[4], f"Wrong discount"
