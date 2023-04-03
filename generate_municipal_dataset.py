from faker import Faker 
import csv

fake = Faker()

with open("data.csv", "a") as f: 
    writer = csv.writer(f)
    
    
    for _ in range(1500):
        Region = fake.state()
        Type = fake.random_element(elements=("Town", "Rural Municipality", "Regional Municipality"))
        Year = fake.year()
        Reliance_on_Government_Transfers = fake.pyfloat(left_digits=1, right_digits=3)
        Uncollected_Taxes = fake.pyfloat(left_digits=1, right_digits=3)
        Three_Year_Change_in_Tax_Base = fake.pyfloat(left_digits=1, right_digits=2)
        Reliance_on_Single_Business_or_Institution = fake.pyfloat(left_digits=1, right_digits=3)
        Residential_Tax_Effort = fake.pyfloat(left_digits=1, right_digits=2)
        Total_Number_of_Deficits = fake.random_int(min=0, max=5)
        Total_Number_of_Budget_Accuracy_within_Plus_or_Minus_5_Percent = fake.random_int(min=-5, max=5) # Assuming this is a percentage difference
        Liquidity = fake.pyfloat(left_digits=1, right_digits=3)
        Operating_Reserve = fake.pyfloat(left_digits=1, right_digits=3)
        Debt_Service_Cost = fake.pyfloat(left_digits=1, right_digits=3)
        Outstanding_Operating_Debt = fake.pyfloat(left_digits=1, right_digits=3)
        Undepreciated_Assets = fake.pyfloat(left_digits=1, right_digits=3)
        Combined_Operating_Capital_Reserves = fake.pyfloat(left_digits=1, right_digits=3)


        writer.writerow([Region, Type, Year, Reliance_on_Government_Transfers, Uncollected_Taxes, 
        Three_Year_Change_in_Tax_Base, Reliance_on_Single_Business_or_Institution, Residential_Tax_Effort, 
        Total_Number_of_Deficits, Total_Number_of_Budget_Accuracy_within_Plus_or_Minus_5_Percent, Liquidity, 
        Operating_Reserve, Debt_Service_Cost, Outstanding_Operating_Debt, Undepreciated_Assets, Combined_Operating_Capital_Reserves])