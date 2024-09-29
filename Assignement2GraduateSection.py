# Load tax brackets from a file
#I used brackets because it easier to track like arrays
def load_tax_brackets(file_path):
    brackets = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            rate = float(lines[i].strip())
            if lines[i + 1].strip().lower() == "inf":
                limit = float('inf')
            else:
                limit = float(lines[i + 1].strip())
            brackets.append((rate, limit))
    return brackets


# Load the tax brackets from the file
#Change file extention
tax_brackets = load_tax_brackets("D:\\tax_bracket.txt")



# Start Outer Loop same as previous section
ConitionForOuterLoop = True

while ConitionForOuterLoop:
    NewUser = str(input("Do You Want To Start New Process ? Yes/No : "))

    if NewUser.lower() == 'yes':
        Name = str(input("Enter your name: "))
        SSN = input("Enter your Social Security Number: ")
        Salary = float(input("Enter your Salary: "))
#************* customer Inforamtion Section Ends *************

        
#*********** SSN validation check Starts *************
        conditionForInnerLoop= True
#Inner Loop To Check For the SSN Validation
        while (conditionForInnerLoop):
            
          if  SSN.isdigit() and len(SSN) == 9:
              
              print("You Have Entered a Valid Social Security Number")
              break
          
          else:
             SSN=input("Invalid SSN Number, Please re-enter your Social Security Number: ")
#*********** SSN validation check ENDS *************


# #************* Calculate Tax *************
        Taxowen = 0.0
        previous_limit = 0.0

        for rate, limit in tax_brackets:
            if Salary > limit:
                taxable_income = limit - previous_limit
            else:
                taxable_income = Salary - previous_limit

            Taxowen += taxable_income * rate

            if Salary <= limit:
                break

            previous_limit = limit

# ************* Function to design and print the receipt *************
        width = 60
        def format_line(title, value):
            dots_count = width - len(title) - len(value) - 2  # 2 accounts for the '|' at both ends
            dots = '.' * dots_count
            return f"|{title}{dots}{value}|"

        #************* Printing Receipt*************
        print("-" * width)
        print(format_line("Name:", Name))
        print(format_line("SSN:", SSN))
        print(format_line("Income:", f"${round(Salary, 2)}"))
        print("-" * width)

        percent = Taxowen / Salary * 100
        tax_statement = f"Federal Income Tax Due: ${round(Taxowen, 2)} ({round(percent, 1)}% of income)"
        
        # Calculate the space needed to align the closing bracket with '|'
        space_needed = width - len(tax_statement)
        print(' ' * space_needed + tax_statement)
        print(" ")  # New Line
        #Check if customer really want to exit the program and he didn't just missplling
    else:
        FinalDesicion = input("Are You Sure You Want To Exit ? Yes/No: ")
        if FinalDesicion.lower() == 'yes':
            print("Alright, Have a Good Day! :)")
            ConitionForOuterLoop = False
