# Assignement 2 Ayoub Eabidawi CSCI536_01

Salary= int(input("Enter your Salary: "))


if Salary <= 11000:
    if Salary - 11000 == 0:
        print("your Salary is 11,000 so there will be 10% Taxes")
    else:
        print("your Salary is less than 11,000 so there will be 10% Taxes")
elif Salary > 11000 and Salary <= 44725:
       
    print("your Salary is between $ 11,000 and $ 44,725, so your taxes will be 12%")
elif Salary >= 44725 and Salary < 95375:
    print("your Salary is between $ 11,000 and $ 44,725, so your taxes will be 12%")
elif Salary >= 95375 and Salary < 182100:
    print("your Salary is between $ 11,000 and $ 44,725, so your taxes will be 12%")
elif Salary >= 182100 and Salary < 231250:
    print("your Salary is between $ 11,000 and $ 44,725, so your taxes will be 12%")
elif Salary >= 231250 and Salary < 578125:
    print("your Salary is between $ 11,000 and $ 44,725, so your taxes will be 12%")
elif  Salary > 578125:
    print("your Salary is between $ 11,000 and $ 44,725, so your taxes will be 12%")
    
