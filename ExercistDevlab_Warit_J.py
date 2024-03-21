RENT = int(input("RENT  :"))
WATER = int(input("WATER :"))
ELEC = int(input("ELEC  :"))
NET = int(input("NET   :"))
PHONE = int(input("PHONE :"))
TOTAL = RENT + WATER + ELEC + NET + PHONE
REMAIN = 2000 - TOTAL

print("RENT  :",RENT ,"฿")
print("WATER :",WATER ,"฿")
print("ELEC  :",ELEC ,"฿")
print("NET   :",NET ,"฿")
print("PHONE :",PHONE ,"฿")
print("TOTAL :",RENT ,"+",WATER ,"+",ELEC ,"+",NET ,"+",PHONE )
print("       ","=",TOTAL,"฿")

if REMAIN >= 10: 
  item = "chewy noodles"
  item_price = 10
elif REMAIN >= 6: 
  item = "instant noodles"
  item_price = 6
elif REMAIN >=2: 
  item = "soup"
  item_price = 2
elif REMAIN >= 0: 
  item = "drinking water"
  item_price = 0
else:
  item = "drinking water"
  item_price = 0

print("SELECT:",item )
print("       ","=" ,item_price ,"฿" )
 
print("SAVING:",2000 , "-",TOTAL ,"-" ,item_price )
print("       " ,"=" ,2000-TOTAL-item_price ,"฿")
