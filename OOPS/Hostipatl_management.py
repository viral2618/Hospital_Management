import pandas as pd
from random import randint
import os

Data=list()


if os.path.exists("save.xlsx"):
    df_existing = pd.read_excel("save.xlsx")
    Data = df_existing.to_dict(orient="records") 


class Hospital:
    hos_name='Mauli Hospital Ltd ' 
    exp=3000
    def __init__(self,patient_name,p_id,bal=0):
        self.balance=bal
        self.patient=patient_name
        self.patient_id=p_id
    
    def Welcome(self):
        print(f"Welcome To {self.hos_name}, {self.patient}")
        
    def Medical_exp(self,med,food):
        self.medicine=med
        self.food=food
        total=med+food
        if total>self.balance:
            print(f"Insufficient balance pay later for food and medicines {self.patient}")
            return False
        self.balance-=total
        print(f"Amount to be paid for food and medicine",total)
        return True
    
    def rent_for_days(self,days):
        self.days=days
        Days_exp=days*self.exp
        if self.balance<Days_exp:
            print(f"Insufficient balance pay later for rented days {self.patient}")
            return False
        self.balance-=Days_exp
        print(f"for {days} Days ,You have to pay {Days_exp}")
        return True
    
    
    def Total_bal(self):
        print("your balance=",self.balance)
        

while True:        
    patient_name=input("enter patient name--")
    patient_id=randint(100,10000)
    AmountDeposit=int(input("Enter an amount to be deposited--"))
    RentDays=int(input("Enter no. of Days Patient Rented--"))
    medical_exp=int(input("Enter amount for medicine expenses--"))
    food_exp=int(input("Enter amount for food expenses--"))
    h1=Hospital(patient_name,patient_id,AmountDeposit)
    print()
    h1.Welcome()
    actual_days = 0
    actual_med = 0
    actual_food = 0

    if h1.rent_for_days(RentDays):
        actual_days = RentDays

    if h1.Medical_exp(medical_exp, food_exp):
        actual_med = medical_exp
        actual_food = food_exp

    h1.Total_bal()
    
    Data.append({
        "Patient Name": patient_name,
        "Patient ID": h1.patient_id,
        "Deposited Amount": AmountDeposit,
        "Rent Days": actual_days,
        "Medicine Expense": actual_med,
        "Food Expense": actual_food,
        "Final Balance": h1.balance
    })
    print("Current Patient Record:-")
    for entry in Data:
        print("Patient id",patient_id)
        

    end=input('\nDo you want to enter another patient? (yes/no):').lower()
    if end != "yes":
        break

df=pd.DataFrame(Data)
df.to_excel("save.xlsx",index=False)
print("\n✅ Data saved to 'save.xlsx' successfully.")
