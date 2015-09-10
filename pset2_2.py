balance = 4773
annualInterestRate = 0.2

unpaid = balance
monthlyPaymentRate = 10

def addInterest(money):
  return annualInterestRate / 12.0 * money

while unpaid >= 0:
  newBalance = balance
  month = 0
  while month < 12:
    unpaid = newBalance - monthlyPaymentRate
    newBalance = unpaid + addInterest(unpaid)
    month = month + 1
  monthlyPaymentRate = monthlyPaymentRate + 10
  
print 'Lowest Payment:', monthlyPaymentRate - 10
