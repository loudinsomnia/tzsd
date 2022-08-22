import pytest


class Discount:
    Discount1 = list(range(0, 100))
    Discount2 = list(range(100, 200))
    Discount3 = list(range(200, 500))


class DiscountCount:
    def discount_counter(self, score):
        if score in Discount.Discount1:
            return '1%'
        elif score in Discount.Discount2:
            return '3%'
        elif score in Discount.Discount3:
            return '5%'
        elif score >= 500:
            return '10%'
        else:
            return False
