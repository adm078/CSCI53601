# Assignement 2 Ayoub Eabidawi CSCI536_01
# Calculate the federal income tax of individual filers. 

Name = str(input("Enter your name: "))
SSN = input("Enter you Social Security Number: ")
Salary= int(input("Enter your Salary: "))
Taxowen = float()
condition = True

while (condition):
    
  if  SSN.isdigit() and len(SSN) == 9:
      
      print("You Entered a Valid Social Security Number")
      break
  
  else:
     SSN=input("Unvalid Number, Please re-enter your Social Security Number")
    


if Salary <= 11000:
    Taxowen = Salary * 0.10
    print("Since your salary is below $11,000, you fall into the 10.0% tax bracket.")
    print(round(Taxowen,2))
    
elif Salary > 11000 and Salary <= 44725:
    Taxowen = (((Salary - 11000)*0.12) + (11000 * 0.10))
    print("Since your salary falls between $11,000 and $44,725, you are in the 12.0% tax bracket.")
    print(round(Taxowen,2))
    
elif Salary > 44725 and Salary <= 95375:
    Taxowen = (((Salary - 44725)*0.22) + ((44725 - 11000)*0.12) + (11000 * 0.10))
    print("Since your salary falls between $44,725 and $95,375, you are in the 22.0% tax bracket.")
    print(round(Taxowen,2))
    
elif Salary > 95375 and Salary <= 182100:
    Taxowen = (((Salary - 95375)*0.24) + ((95375 - 44725)*0.22) + ((44725 - 11000)*0.12) + (11000 * 0.10))
    print("Since your salary falls between $95,375 and $182,100, you are in the 24.0% tax bracket.")
    print(round(Taxowen,2))
    
elif Salary > 182100 and Salary <= 231250:
    Taxowen = ( ((Salary - 182100)*0.32) + ((182100 - 95375)*0.24) + ((95375 - 44725)*0.22) + ((44725 - 11000)*0.12) + (11000 * 0.10))
    print("Since your salary falls between $182,100 and $231,250, you are in the 32.0% tax bracket.")
    print(round(Taxowen,2))
    
elif Salary > 231250 and Salary <= 578125:
    Taxowen = (((Salary - 231250)*0.35) + ((231250 - 182100)*32) + ((182100 - 95375)*0.24) + ((95375 - 44725)*0.22) + ((44725 - 11000)*0.12) + (11000 * 0.10))
    print("Since your salary falls between $231,250 and $578,125, you are in the 35.0% tax bracket.")
    print(round(Taxowen,2))
    
elif  Salary > 578125:
    Taxowen = (((Salary-578125)*0.37) + ((578125 - 231250)*0.35) + ((231250 - 182100)*32) + ((182100 - 95375)*0.24) + ((95375 - 44725)*0.22) + ((44725 - 11000)*0.12) + (11000 * 0.10))
    print("Since your salary is over $578,125, you are in the 37.0% tax bracket.")
    print(round(Taxowen,2))
    
print("-------------------------------------------")
print ("|Name:.................................."   ,Name   , "|")
print ("|SSN:.................................."    ,SSN    , "|")
print ("|Income:................................" ,round(Salary,2) , "|")
print("-------------------------------------------")