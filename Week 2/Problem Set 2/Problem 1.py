for i in range(12):
    monIntRate = annualInterestRate / 12
    minMonPay = monthlyPaymentRate * balance
    monUnpBal = balance - minMonPay
    balance = monUnpBal + monIntRate * monUnpBal

print(round(balance, 2))

