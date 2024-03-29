from forex_python.converter import CurrencyRates
c = CurrencyRates()
c.get_rates('USD')   # you can directly call get_rates('USD')
{u'IDR': 13625.0, u'BGN': 1.7433, u'ILS': 3.8794, u'GBP': 0.68641, u'DKK': 6.6289, u'CAD': 1.3106, u'JPY': 110.36, u'HUF': 282.36, u'RON': 4.0162, u'MYR': 4.081, u'SEK': 8.3419, u'SGD': 1.3815, u'HKD': 7.7673, u'AUD': 1.3833, u'CHF': 0.99144, u'KRW': 1187.3, u'CNY': 6.5475, u'TRY': 2.9839, u'HRK': 6.6731, u'NZD': 1.4777, u'THB': 35.73, u'EUR': 0.89135, u'NOK': 8.3212, u'RUB': 66.774, u'INR': 67.473, u'MXN': 18.41, u'CZK': 24.089, u'BRL': 3.5473, u'PLN': 3.94, u'PHP': 46.775, u'ZAR': 15.747}

import datetime

print("Welcome to Currency MAX., MIN.,and Average Calculation PROGRAM for USD to THB in Year 2023")
mm = int(input("Year 2023 of preferred month(select 1-12):"))

if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
    dd = 31
elif mm == 2:
    if mm % 4 == 0: dd = 29
    else: dd = 28
else:
    dd = 30

minrate = 0
mindate = ""
maxrate = 0
maxdate = ""
avgrate = 0
totalrate = 0
tempcrr = 0
currencyrate = []
currencydate = []

for dd in range(dd):
    date_obj = datetime.datetime(2023, mm, dd+1, 18, 00, 00, 000000)
    tempcrr = c.get_rate('USD', 'THB', date_obj)  # get_rate('USD', 'INR', date_obj)
    tempdate = "2023" + "." + str(mm) + "." + str(dd + 1)
    totalrate += tempcrr
    avgrate = totalrate/(dd+1)

    if maxrate > 0:
        if tempcrr > maxrate:
            maxrate = tempcrr
            maxdate = tempdate
    else:
        maxrate = tempcrr

    if minrate > 0:
        if tempcrr < minrate:
            minrate = tempcrr
            mindate = tempdate
    else:
        minrate = tempcrr

    currencyrate.append(tempcrr)
    currencydate.append(tempdate)
    print(currencydate[dd], currencyrate[dd])

print("Minimum exchangerate from USD to THB:", minrate, "on the date", mindate)
print("Maximum exchangerate from USD to THB:", maxrate,"on the date", maxdate)
print("Average exchange rate from USD to THB:", avgrate)

