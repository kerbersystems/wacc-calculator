import random
res = 1.0

coe = float(input('Current Cost of Equity: '))/100
pcoelow = float(input('% Equity Lower Limit: '))/100
pcoeupper = float(input('% Equity Upper Limit: '))/100

cod = float(input('Current Cost of Debt: '))/100
pcodlow = float(input('% Debt Lower Limit: '))/100
pcodupper = float(input('% Debt Upper Limit: '))/100

cops = float(input('Current Cost of Prefered Stock: '))/100
pcopslow = float(input('% Prefered Stock Lower Limit: '))/100
pcopsupper = float(input('% Prefered Stock Upper Limit: '))/100
tax = float(input('Tax Rate: '))/100

targetrate = float(input('Target Rate: '))/100

while res != targetrate:
    i = round(random.uniform(pcoelow, pcoeupper), 2)
    j = round(random.uniform(pcodlow, pcodupper), 2)
    k = round(random.uniform(pcopslow, pcopsupper), 2)
    res = round((coe * i) + (cops * k) + ((cod * (1 -tax)) * j), 3)
    
    if (i + j + k) == 1.0:
        if (res == targetrate):
            print('To acheive a WACC of ' + str(100 * targetrate) + "% the following percentages are needed.")
            print("%COE= " + str(i) + " %COD= " + str(j) + " %COPS= " + str(k))
    else:
        res = 1.0
