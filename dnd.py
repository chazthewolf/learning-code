import random

coinflip = ["Heads (1)", "Tails (2)"]

dTwo = random.choice(coinflip)
dFour = random.randint(1,4)
dSix = random.randint(1,6)
dEight = random.randint(1,8)
dTen = random.randint(1,10)
dTwelve = random.randint(1,12)
dTwenty = random.randint(1,20)
dHundred = random.randint(1,100)

print("d2: {}".format(dTwo))
print("d4: {}".format(dFour))
print("d6: {}".format(dSix))
print("d8: {}".format(dEight))
print("d10: {}".format(dTen))
print("d12: {}".format(dTwelve))
print("d20: {}".format(dTwenty))
print("d100: {}".format(dHundred))