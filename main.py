# Program calculates pay sums, overpay and total pay for 2 different types of credit:
# with annuity payment, or with differentiated payment.

# Importing localization file.
import local as lc

# Input section.
kind_of_payments = int(input(lc.KIND_OF_PAYMENTS))
while kind_of_payments > 2 or kind_of_payments < 1:
    print(lc.ERR_1)
    kind_of_payments = int(input(lc.KIND_OF_PAYMENTS))
sum_ = float(input(lc.SUM))
while sum_ < 10_000:
    print(lc.ERR_2)
    sum_ = int(input(lc.SUM))
interest = float(input(lc.INTEREST_RATE)) / 12 / 100
while interest < 0:
    print(lc.ERR_3)
    interest = float(input(lc.INTEREST_RATE)) / 12 / 100
month = float(input(lc.MONTH))
while month <= 0 or month != int(month):
    print(lc.ERR_4)
    month = float(input(lc.MONTH))
commission = float(input(lc.COMMISSION)) / 100
while commission < 0:
    print(lc.ERR_5)
    commission = float(input(lc.COMMISSION)) / 100

month = int(month)

if kind_of_payments == 1:
    # Calculating annuity payment using formula.
    annuity_payment = sum_ * (interest + (interest / (((1 + interest) ** month) - 1)))
    # Calculating other items.
    pay_sum = annuity_payment * month + commission * sum_
    overpay = pay_sum - sum_
    # Output section.
    print(lc.OUT_1, round(annuity_payment, 2), lc.CURRENCY)
    print(lc.OUT_2, round(overpay, 2), lc.CURRENCY)
    print(lc.OUT_3, round(pay_sum, 2), lc.CURRENCY)

else:
    solid_payment = sum_ / month
    month_interest = 0
    rest_of_credit = sum_
    pay_sum = 0
    # Calculating and printing month pay sums for each month. Collecting all of them into full pay sum.
    for num in range(1, month + 1):
        month_interest = rest_of_credit * interest
        month_payment = solid_payment + month_interest
        rest_of_credit -= month_payment
        pay_sum += month_payment
        print(lc.PREPOSITION, num, lc.MONTH_1, round(month_payment, 2), lc.CURRENCY)
    # Calculating other items.
    pay_sum += commission * sum_
    overpay = pay_sum - sum_
    # Output section.
    print(lc.OUT_2, round(overpay, 2), lc.CURRENCY)
    print(lc.OUT_3, round(pay_sum, 2), lc.CURRENCY)
