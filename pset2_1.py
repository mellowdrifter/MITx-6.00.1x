balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPaid = 0
month = 1

def minPayment(money):
  return round(money * monthlyPaymentRate, 2)

def interestPaid(money):
  return round(annualInterestRate / 12.0 * money, 2)


while month <= 12:
  print 'Month:', month
  minpay = minPayment(balance)
  unpaid = balance - minpay
  interest = interestPaid(unpaid)
  totalPaid = totalPaid + minpay

  print 'Minimum monthly payment:', minpay
  print 'Remaining balance:', unpaid + interest
  if month == 12:
    print 'Total paid:', totalPaid
    print 'Remaining balance:', unpaid + interest


  balance = balance - minpay + interest
  month = month + 1
