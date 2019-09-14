updBalance = balance
monFixPay = 0

while updBalance >= 0:
    updBalance = balance
    monFixPay += 10
    for i in range(12):
        monIntRate = annualInterestRate / 12
        monUnpBal = updBalance - monFixPay
        updBalance = monUnpBal + monIntRate * monUnpBal

print("Lowest Payment:", monFixPay)

