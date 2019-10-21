# This
# 4
# 4 annuity payment annuity payment annuity payment
import local as lc

# Input section.
print(lc.INTRO)
sum_ = float(input(lc.SUM))
while sum_ < 10_000:
    print(lc.ERR_1)
    sum_ = int(input(lc.SUM))
interest = float(input(lc.INTEREST_RATE)) / 12 / 100
while interest < 0:
    print(lc.ERR_2)
    interest = int(input(lc.INTEREST_RATE))
month = float(input(lc.MONTH))
while month <= 0 or month != int(month):
    print(lc.ERR_3)
    month = float(input(lc.MONTH))
commission = float(input(lc.COMMISSION)) / 100

# Calculating annuity payment using formula.
annuity_payment = sum_ * (interest + (interest / (((1 + interest) ** month) - 1)))

# Calculating other items.
pay_sum = annuity_payment * month + commission * sum_
overpay = pay_sum - sum_

# Output section.
print(lc.OUT_1, round(annuity_payment, 2), lc.CURRENCY)
print(lc.OUT_2, round(overpay, 2), lc.CURRENCY)
print(lc.OUT_3, round(pay_sum, 2), lc.CURRENCY)
