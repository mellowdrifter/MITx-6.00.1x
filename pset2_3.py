import math

balance = 999999
annualInterestRate = 0.18

unpaid = balance
lowAmount = balance / 12
highAmount = balance * math.pow((1 + annualInterestRate / 12), 12) / 12.0


def addInterest(money):
  return annualInterestRate / 12.0 * money

while unpaid != 0:
  monthlyPaymentRate = (highAmount + lowAmount) / 2
  newBalance = balance
  month = 0
  while month < 12:
    unpaid = newBalance - monthlyPaymentRate
    newBalance = unpaid + addInterest(unpaid)
    month += 1

  if round(unpaid, 2)  > 0:
    lowAmount = monthlyPaymentRate
  elif round(unpaid, 2) < 0:
    highAmount = monthlyPaymentRate
  elif round(unpaid, 2) == 0:
    unpaid = 0

print 'Lowest Payment: %.2f' % (monthlyPaymentRate - 0.01)
