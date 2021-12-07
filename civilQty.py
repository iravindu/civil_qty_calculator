import math
import time
import pandas as pd
import xlsxwriter 

blockPrice = 45
cementPrice = 1350
sandPrice = 16700

qtyList = []
costList = []
descriptionList = []

print("Civil Quantity Calculator")
print("----------------------------------")

i = 'y'
while i =='y':
    
    if i =='y':
        inputQty = float(input("Please Enter Wall Area in sq.m :" ))
        inputDesc = input("Please Enter Description :" )
        print("                                   ")
    
        blockQty = round(inputQty * 15,2)
        cementQty = round(inputQty * 0.2,2)
        sandQty = round(inputQty * 0.01,2)
        laborCost = round(inputQty * 490,2)

        totalCost = (blockQty * blockPrice) + (cementQty * cementPrice) + (sandQty * sandPrice) + laborCost

        qtyList.append(inputQty)
        costList.append(totalCost)
        descriptionList.append(inputDesc)
        i = input(("Do you want to continue? (Y/N) : "))

boqDict = {'Description': descriptionList, 'Quantity': qtyList, 'Amount': costList}

df = pd.DataFrame(boqDict)

writer = pd.ExcelWriter('boq.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='civil')
# worksheet = writer.sheets['civil']

writer.save()
# print(quantities)    