monIntRate = annualInterestRate / 12
updBalance = balance
monLowBound = updBalance / 12
monUppBound = (updBalance * (1 + monIntRate) ** 12) / 12

while round(updBalance, 2) != 0:
    updBalance = balance
    monFixPay = (monLowBound + monUppBound) / 2
    for i in range(12):
        monUnpBal = updBalance - monFixPay
        updBalance = monUnpBal + monIntRate * monUnpBal
    if updBalance > 0:
        monLowBound = monFixPay
    elif updBalance < 0:
        monUppBound = monFixPay

print("Lowest Payment:", round(monFixPay, 2))