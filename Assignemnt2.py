# Assignement 2 Ayoub Eabidawi CSCI536_01
# Calculate the federal income tax of individual filers. 

#Part 1
ConitionForOuterLoop = True

#outer Loop 
while (ConitionForOuterLoop):
    NewUser= str(input("Do You Want To Start New Process ? Yes/No : ")) 
    
#Check If the user wants to  Repeat the process
    if  NewUser.lower()== 'yes':
        Name = str(input("Enter your name: "))
        SSN = input("Enter you Social Security Number: ")
        Salary= float(input("Enter your Salary: "))
        Taxowen = float()
        percent = 1.0
        conditionForInnerLoop = True
        
        
#Inner Loop To Check For the SSN Validation
        while (conditionForInnerLoop):
            
          if  SSN.isdigit() and len(SSN) == 9:
              
              print("You Have Entered a Valid Social Security Number")
              break
          
          else:
             SSN=input("Unvalid Number, Please re-enter your Social Security Number: ")
            
        
#To Check what tax percentage will be applied to the salary
        if Salary>0 and Salary <= 11000:
            percent = 10.0
            Taxowen = Salary * 0.10
            print("Since your salary is below $11,000, you fall into the 10.0% tax bracket.")
            print(round(Taxowen,2))
            
        elif Salary > 11000 and Salary <= 44725:
            percent = 12.0
            Taxowen = (((Salary - 11000)*0.12) + (11000 * 0.10))
            print("Since your salary falls between $11,000 and $44,725, you are in the 12.0% tax bracket.")
            print(round(Taxowen,2))
            
        elif Salary > 44725 and Salary <= 95375:
            percent = 22.0
            Taxowen = (((Salary - 44725)*0.22) + ((44725 - 11000)*0.12) + (11000 * 0.10))
            print("Since your salary falls between $44,725 and $95,375, you are in the 22.0% tax bracket.")
            print(round(Taxowen,2))
            
        elif Salary > 95375 and Salary <= 182100:
            percent = 24.0
            Taxowen = (((Salary - 95375)*0.24) + ((95375 - 44725)*0.22) + ((44725 - 11000)*0.12) + (11000 * 0.10))
            print("Since your salary falls between $95,375 and $182,100, you are in the 24.0% tax bracket.")
            print(round(Taxowen,2))
            
        elif Salary > 182100 and Salary <= 231250:
            percent = 32.0
            Taxowen = ( ((Salary - 182100)*0.32) + ((182100 - 95375)*0.24) + ((95375 - 44725)*0.22) + ((44725 - 11000)*0.12) + (11000 * 0.10))
            print("Since your salary falls between $182,100 and $231,250, you are in the 32.0% tax bracket.")
            print(round(Taxowen,2))
            
        elif Salary > 231250 and Salary <= 578125:
            percent = 35.0
            Taxowen = (((Salary - 231250)*0.35) + ((231250 - 182100)*32) + ((182100 - 95375)*0.24) + ((95375 - 44725)*0.22) + ((44725 - 11000)*0.12) + (11000 * 0.10))
            print("Since your salary falls between $231,250 and $578,125, you are in the 35.0% tax bracket.")
            print(round(Taxowen,2))
            
        elif  Salary > 578125:
            percent = 37.0
            Taxowen = (((Salary-578125)*0.37) + ((578125 - 231250)*0.35) + ((231250 - 182100)*32) + ((182100 - 95375)*0.24) + ((95375 - 44725)*0.22) + ((44725 - 11000)*0.12) + (11000 * 0.10))
            print("Since your salary is over $578,125, you are in the 37.0% tax bracket.")
            print(round(Taxowen,2))
            
        # To Check if salary legit 
        else:
            print("Your Salary cant be 0 or negative!")
            Salary= float(input("Please Re-Enter your Salary: "))
            if Salary <=0:
                print("Bye")
                break
#End of Condition

            
#Function to design and print the recepit beginning
        width = 60 
        def format_line(title, value):
            dots_count = width - len(title) - len(value) - 2  # 2 accounts for the '|' at both ends
            dots = '.' * dots_count
            return f"|{title}{dots}{value}|"
#Function Ends


#Printing Recepit starts
        print("-" * width)
        print(format_line("Name:", Name))
        print(format_line("SSN:", SSN))
        print(format_line("Income:", f"${round(Salary, 2)}"))
        print("-" * width)
        percent = Taxowen / Salary
        percent = percent*100
        tax_statement = f"Federal Income Tax Due: ${round(Taxowen, 2)} ({round(percent, 1)}% of income)"
# Calculate the space needed to align the closing bracket with '|'
        space_needed = width - len(tax_statement)
        print(' ' * space_needed + tax_statement)  # Right-align by adding leading spaces
#Printing Recepit Ends   
     
        print(" ") # NEW Line
        
        
#Making sure that user really wants to quit the application        
    else:
         FinalDesicion = input("Are You Sure You Want To Exit ? ")
         if FinalDesicion.lower()== 'yes':
            print("Alright, Have a Good Day ! :)")
            ConitionForOuterLoop= False
         else:
            print("Okay Make Sure to Answer Yes with the correct splling")
            continue
         
#*********************** PART 2 ***********************


