# Assignement 2 Ayoub Eabidawi CSCI536_01
# Name = str(input("Enter your name: "))
# SSN = int(input("Enter you Social Security Number: "))
Salary= int(input("Enter your Salary: "))


if Salary <= 11000:
    Taxowen = Salary * 0.10
    print("your Salary is between $ 11,000 and $ 44,725, so your taxes will be 10%") 
    print(Taxowen)
    
elif Salary > 11000 and Salary <= 44725:
    Taxowen = (((Salary - 11000)*0.12) + (11000 * 0.10))
    print("your Salary is between $ 11,000 and $ 44,725, so your taxes will be 12%")
    print(Taxowen)
    
elif Salary > 44725 and Salary <= 95375:
    Taxowen = (((Salary - 44725)*0.22) + ((44725 - 11000)*0.12) + (11000 * 0.10))
    print("your Salary is between $ 44,725 and $ 95,375 so your taxes will be 22%")
    print(Taxowen)
    
elif Salary > 95375 and Salary <= 182100:
    Taxowen = (((Salary - 95375)*0.24) + ((95375 - 44725)*0.22) + ((44725 - 11000)*0.12) + (11000 * 0.10))
    print("your Salary is between $ 95,375 and $ 182,100, so your taxes will be 24%")
    print(Taxowen)
    
elif Salary > 182100 and Salary <= 231250:
    Taxowen = ( ((Salary - 182100)*0.32) + ((182100 - 95375)*0.24) + ((95375 - 44725)*0.22) + ((44725 - 11000)*0.12) + (11000 * 0.10))
    print("your Salary is between $ 182,100 and $ 231,250 so your taxes will be 32%")
    print(Taxowen)
    
elif Salary > 231250 and Salary <= 578125:
    Taxowen = (((Salary - 231250)*0.34) + ((231250 - 182100)*32) + ((182100 - 95375)*0.24) + ((95375 - 44725)*0.22) + ((44725 - 11000)*0.12) + (11000 * 0.10))
    print("your Salary is between $ 231,250 and $ 578,125 so your taxes will be 34%")
    print(Taxowen)
    
elif  Salary > 578125:
    Taxowen = (((Salary-578125)*0.36) + ((578125 - 231250)*0.34) + ((231250 - 182100)*32) + ((182100 - 95375)*0.24) + ((95375 - 44725)*0.22) + ((44725 - 11000)*0.12) + (11000 * 0.10))
    print("your Salary is more than $ 578,125 So your tax rate will be 36%")
    print(Taxowen)
    
    
