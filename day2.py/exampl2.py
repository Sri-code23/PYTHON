loan = -1  # Initialize with an invalid value
eligible = False  # Flag to check if the user is eligible

while not eligible:
    # Collect user input for salary and age
    salary = int(input("Enter your salary: "))
    age = int(input("Enter your age: "))
    
    # Check eligibility criteria
    if salary >= 20000 or age <= 25:
        eligible = True  # Set eligible flag to True
        while loan < 0 or loan > 50000:
            # Prompt for loan amount
            loan = float(input("Enter the required loan amount: "))
            
            # Check if the requested loan amount is within the limit
            if loan <= 50000:
                print("You are eligible for the loan.")
            else:
                print("The maximum loan amount is up to 50,000.")
                loan = -1  # Reset loan to ensure the user is prompted again for loan amount
    else:
        print("You are not eligible for the loan.")
        eligible = True  # Exit the outer loop if not eligible
